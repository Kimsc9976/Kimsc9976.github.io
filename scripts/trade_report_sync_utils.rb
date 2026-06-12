# frozen_string_literal: true

require "yaml"
require "fileutils"
require "digest"
require "time"
require "date"

module TradeReportSync
  ROOT          = File.expand_path("..", __dir__)
  CONFIG_PATH   = File.join(ROOT, "_data", "trade_report_sync.yml")
  DEFAULT_SOURCE = File.join(ROOT, "modules", "trade_report")

  module_function

  def load_config
    YAML.load_file(CONFIG_PATH)
  end

  # "> 생성 시각: 2026-05-27 08:23:15" 패턴에서 Time 추출
  def parse_generated_at(body)
    m = body.match(/>\s*생성\s*시각:\s*(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})/)
    return nil unless m

    Time.strptime("#{m[1]} #{m[2]}", "%Y-%m-%d %H:%M:%S")
  rescue ArgumentError
    nil
  end

  # front matter hash + body string → Jekyll md string
  def render_page(front_matter, body)
    body = body.sub(/\A\s+/, "").sub(/\s+\z/, "")
    fm_yaml = front_matter.to_yaml.sub(/\A---\n/, "").sub(/\n\.\.\.\z/, "").rstrip
    "---\n#{fm_yaml}\n---\n\n#{body}\n"
  end

  # 내용이 변경된 경우에만 파일 쓰기
  def write_if_changed(out_path, content, dry_run:)
    new_digest = Digest::SHA256.hexdigest(content)
    if File.exist?(out_path)
      return :skipped if Digest::SHA256.hexdigest(File.read(out_path, encoding: "UTF-8")) == new_digest
    end

    if dry_run
      puts "[dry-run] #{out_path}"
    else
      FileUtils.mkdir_p(File.dirname(out_path))
      File.write(out_path, content, encoding: "UTF-8")
      puts "wrote    #{out_path}"
    end
    :written
  end

  # 바이너리(PNG 등) 변경 시에만 복사
  def copy_if_changed(src, dst, dry_run:)
    return :skipped unless File.exist?(src)

    if File.exist?(dst) && Digest::SHA256.file(src) == Digest::SHA256.file(dst)
      return :skipped
    end

    if dry_run
      puts "[dry-run] copy #{src} -> #{dst}"
    else
      FileUtils.mkdir_p(File.dirname(dst))
      FileUtils.cp(src, dst)
      puts "copied   #{dst}"
    end
    :written
  end

  def parse_since(since_str)
    return nil if since_str.to_s.strip.empty?

    Date.parse(since_str)
  rescue ArgumentError
    abort "ERROR: --since 날짜 형식 오류: #{since_str}"
  end

  def date_str(year, month, day)
    format("%04d-%02d-%02d", year.to_i, month.to_i, day.to_i)
  end

  # YYYY/MM/DD 구조의 하위 디렉터리 목록 반환
  def day_dirs(root)
    Dir.glob(File.join(root, "*", "*", "*"))
       .select { |p| File.directory?(p) }
       .sort
  end

  # 디렉터리 경로에서 [year, month, day] 파싱
  def parts_from_dir(dir, root)
    rel = dir.sub(%r{\A#{Regexp.escape(root)}[/\\]?}, "")
    rel.split(%r{[/\\]})
  end

  # daily-report 세션 파일: morning.md 우선, 없으면 YYYY-MM-DD_morning.md
  def resolve_session_src(day_dir, date, session_key)
    [
      File.join(day_dir, "#{session_key}.md"),
      File.join(day_dir, "#{date}_#{session_key}.md")
    ].find { |path| File.exist?(path) }
  end

  # journal 단일 파일: journal.md 우선, 없으면 YYYY-MM-DD_journal.md
  def resolve_journal_src(day_dir, date)
    [
      File.join(day_dir, "journal.md"),
      File.join(day_dir, "#{date}_journal.md")
    ].find { |path| File.exist?(path) }
  end

  # charts/*.png → assets/images/trade/journal/{date}/ (파일명 → 웹 경로)
  def sync_journal_charts(day_dir, chart_output_dir, date, charts_subdir: "charts", dry_run: false)
    charts_dir = File.join(day_dir, charts_subdir)
    return {} unless Dir.exist?(charts_dir)

    dest_dir = File.join(chart_output_dir, date)
    web_base = "/assets/images/trade/journal/#{date}"
    mapping  = {}

    Dir.glob(File.join(charts_dir, "*.png")).sort.each do |src|
      fname = File.basename(src)
      dest  = File.join(dest_dir, fname)
      copy_if_changed(src, dest, dry_run: dry_run)
      mapping[fname] = "#{web_base}/#{fname}"
    end
    mapping
  end

  # md 내 charts/… 상대경로 → Jekyll 절대 URL
  def rewrite_journal_chart_refs(body, date)
    web_base = "/assets/images/trade/journal/#{date}"
    body.gsub(/!\[([^\]]*)\]\(([^)]+)\)/) do
      alt  = Regexp.last_match(1)
      href = Regexp.last_match(2).strip
      next Regexp.last_match(0) if href.start_with?("http", "/", "data:")

      fname = File.basename(href.split("#").first.split("?").first)
      next Regexp.last_match(0) unless fname.match?(/\A[\w.-]+\.png\z/i)

      "![#{alt}](#{web_base}/#{fname})"
    end
  end

  SECTION_LABELS = {
    "morning"   => "오전",
    "afternoon" => "오후",
    "journal"   => nil
  }.freeze

  SECTION_ORDER = %w[morning afternoon journal].freeze

  # 단일 journal md 우선, 없으면 morning/afternoon 등 다중 파일 병합
  def collect_journal_body(day_dir, date)
    single = resolve_journal_src(day_dir, date)
    if single
      content = File.read(single, encoding: "UTF-8")
      return { body: content, generated_at: parse_generated_at(content) }
    end

    files = Dir.glob(File.join(day_dir, "*.md"))
               .reject { |f| File.basename(f).match?(/\Areadme\.md\z/i) }
               .sort_by { |f|
                 base = File.basename(f, ".md")
                 idx  = SECTION_ORDER.index(base)
                 idx ? [0, idx] : [1, base]
               }
    return nil if files.empty?

    if files.size == 1 && File.basename(files.first, ".md") == "journal"
      content = File.read(files.first, encoding: "UTF-8")
      return { body: content, generated_at: parse_generated_at(content) }
    end

    sections = files.map do |f|
      base    = File.basename(f, ".md")
      content = File.read(f, encoding: "UTF-8").strip
      label   = SECTION_LABELS.fetch(base, base)
      label ? "## #{label}\n\n#{content}" : content
    end

    latest = files.filter_map { |f| parse_generated_at(File.read(f, encoding: "UTF-8")) }.max
    { body: sections.join("\n\n---\n\n"), generated_at: latest }
  end
end
