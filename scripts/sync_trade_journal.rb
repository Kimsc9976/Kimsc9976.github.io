#!/usr/bin/env ruby
# frozen_string_literal: true

# trade_report/journal/YYYY/MM/DD/journal.md (또는 morning.md + afternoon.md)
# → sideproject/trade/journal/YYYY-MM-DD.md
# chart.png → assets/images/trade/journal/YYYY-MM-DD-chart.png

require "optparse"
require_relative "trade_report_sync_utils"

options = {
  dry_run: false,
  since: nil,
  source: ENV["TRADE_REPORT_SOURCE"]
}

OptionParser.new do |opts|
  opts.banner = "Usage: ruby scripts/sync_trade_journal.rb [options]"

  opts.on("--source PATH", "trade_report 경로 (기본: modules/trade_report)") { |v| options[:source] = v }
  opts.on("--since DATE", "YYYY-MM-DD 이후만 동기화") { |v| options[:since] = v }
  opts.on("--dry-run", "파일 쓰기 없이 변경 목록만 출력") { options[:dry_run] = true }
end.parse!

options[:source] = TradeReportSync::DEFAULT_SOURCE if options[:source].to_s.empty?

source_root = File.expand_path(options[:source])
abort "ERROR: source not found: #{source_root}" unless Dir.exist?(source_root)

config = TradeReportSync.load_config
journal_cfg = config.fetch("journal")
journal_root = File.join(source_root, journal_cfg["source_root"])
output_dir = File.join(TradeReportSync::ROOT, journal_cfg["output_dir"])
chart_output_dir = File.join(TradeReportSync::ROOT, journal_cfg["chart_output_dir"])
since_date = TradeReportSync.parse_since(options[:since])

def collect_day_body(day_dir, sessions_order)
  journal_file = File.join(day_dir, "journal.md")
  if File.exist?(journal_file)
    return {
      body: File.read(journal_file, encoding: "UTF-8"),
      mode: :single
    }
  end

  labels = { "morning" => "오전", "afternoon" => "오후" }
  parts = sessions_order.filter_map do |session|
    path = File.join(day_dir, "#{session}.md")
    next unless File.exist?(path)

    body = File.read(path, encoding: "UTF-8").strip
    "## #{labels[session]}\n\n#{body}"
  end

  {
    body: parts.join("\n\n---\n\n"),
    mode: :merged
  }
end

def resolve_journal_date(day_dir, date_str, sessions_order, default_time)
  times = sessions_order.filter_map do |session|
    path = File.join(day_dir, "#{session}.md")
    next unless File.exist?(path)

    TradeReportSync.parse_generated_at(File.read(path, encoding: "UTF-8"))
  end

  journal_path = File.join(day_dir, "journal.md")
  if File.exist?(journal_path)
    t = TradeReportSync.parse_generated_at(File.read(journal_path, encoding: "UTF-8"))
    times << t if t
  end

  latest = times.compact.max
  return latest.strftime("%Y-%m-%d %H:%M:%S %z") if latest

  "#{date_str} #{default_time}"
end

def build_front_matter(date_str, body, chart_path, mode:)
  title = "#{date_str} 매매일지"
  if mode == :single
    h1 = body.lines.find { |l| l.start_with?("# ") }
    if h1
      cleaned = h1.sub(/^#\s+/, "").strip
      title = cleaned unless cleaned.empty?
    end
  end

  fm = {
    "layout" => "sideproject",
    "title" => title,
    "project" => "trade",
    "trade_section" => "journal",
    "date" => nil,
    "parent_url" => "/sideproject/trade/journal/",
    "permalink" => "/sideproject/trade/journal/#{date_str}/",
    "tags" => ["trade", "journal"],
    "journal_date" => date_str,
    "source" => "trade_report",
    "auto_generated" => true
  }
  fm["chart"] = chart_path if chart_path
  fm
end

def prepend_chart_section(body, title, chart_web_path)
  return body if body.include?(chart_web_path)

  <<~MD.strip + "\n\n#{body.strip}\n"
    ## 📈 Buy / Sell 차트

    ![#{title}](#{chart_web_path}){: .trade-chart}
  MD
end

day_dirs = Dir.glob(File.join(journal_root, "*", "*", "*"))
              .select { |p| File.directory?(p) }
              .sort

if day_dirs.empty?
  warn "WARN: no journal day folders under #{journal_root}"
  exit 0
end

written = 0
skipped = 0
sessions_order = journal_cfg.fetch("sessions_order", %w[morning afternoon])
chart_name = journal_cfg.fetch("chart_source_name", "chart.png")

day_dirs.each do |day_dir|
  rel = day_dir.sub(%r{\A#{Regexp.escape(journal_root)}[/\\]?}, "")
  year, month, day = rel.split(%r{[/\\]})
  date_str = TradeReportSync.date_from_parts(year, month, day)

  if since_date && Date.parse(date_str) < since_date
    skipped += 1
    next
  end

  body_payload = collect_day_body(day_dir, sessions_order)
  body = body_payload[:body]
  if body.strip.empty?
    skipped += 1
    next
  end

  chart_src = File.join(day_dir, chart_name)
  chart_web_path = "/assets/images/trade/journal/#{date_str}-chart.png"
  chart_dest = File.join(chart_output_dir, "#{date_str}-chart.png")

  chart_result = TradeReportSync.copy_if_changed(
    chart_src,
    chart_dest,
    dry_run: options[:dry_run]
  )
  written += 1 if chart_result == :written

  front_matter = build_front_matter(
    date_str,
    body,
    File.exist?(chart_src) ? chart_web_path : nil,
    mode: body_payload[:mode]
  )
  front_matter["date"] = resolve_journal_date(day_dir, date_str, sessions_order, journal_cfg["default_time"])

  final_body = if File.exist?(chart_src)
                 prepend_chart_section(body, front_matter["title"], chart_web_path)
               else
                 body
               end

  out_path = File.join(output_dir, "#{date_str}.md")
  content = TradeReportSync.render_page(front_matter, final_body)
  result = TradeReportSync.write_if_changed(out_path, content, dry_run: options[:dry_run])

  if result == :written
    written += 1
  else
    skipped += 1
  end
end

puts "done: written=#{written} skipped=#{skipped}"
