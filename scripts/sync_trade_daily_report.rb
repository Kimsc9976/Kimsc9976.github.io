#!/usr/bin/env ruby
# frozen_string_literal: true

# trade_report/daily-report/YYYY/MM/DD/{morning,afternoon}.md
# → sideproject/trade/daily-report/YYYY-MM-DD-{am,pm}.md (Jekyll front matter)

require "optparse"
require_relative "trade_report_sync_utils"

options = {
  dry_run: false,
  since: nil,
  update_config: false,
  remote_sha: nil,
  source: ENV["TRADE_REPORT_SOURCE"]
}

OptionParser.new do |opts|
  opts.banner = "Usage: ruby scripts/sync_trade_daily_report.rb [options]"

  opts.on("--source PATH", "trade_report 경로 (기본: modules/trade_report)") { |v| options[:source] = v }
  opts.on("--since DATE", "YYYY-MM-DD 이후만 동기화") { |v| options[:since] = v }
  opts.on("--dry-run", "파일 쓰기 없이 변경 목록만 출력") { options[:dry_run] = true }
  opts.on("--update-config", "last_synced_sha 갱신") { options[:update_config] = true }
  opts.on("--remote-sha SHA", "동기화 완료 후 기록할 원격 커밋 SHA") { |v| options[:remote_sha] = v }
end.parse!

options[:source] = TradeReportSync::DEFAULT_SOURCE if options[:source].to_s.empty?

source_root = File.expand_path(options[:source])
abort "ERROR: source not found: #{source_root}" unless Dir.exist?(source_root)

config = TradeReportSync.load_config
daily_root = File.join(source_root, config["source_root"])
output_dir = File.join(TradeReportSync::ROOT, config["output_dir"])
since_date = TradeReportSync.parse_since(options[:since])

def build_front_matter(date_str, session_key, config, body)
  sess = config["sessions"][session_key]
  generated = TradeReportSync.parse_generated_at(body)
  date_field = if generated
                 generated.strftime("%Y-%m-%d %H:%M:%S %z")
               else
                 "#{date_str} #{sess['default_time']}"
               end

  title = "#{date_str} 일간 레포트 (#{sess['session_label']})"
  h1 = body.lines.find { |l| l.start_with?("# ") }
  if h1
    cleaned = h1.sub(/^#\s+/, "").strip
    title = cleaned unless cleaned.empty?
  end

  {
    "layout" => "sideproject",
    "title" => title,
    "project" => "trade",
    "trade_section" => "daily-report",
    "session" => sess["session"],
    "session_label" => sess["session_label"],
    "date" => date_field,
    "parent_url" => "/sideproject/trade/daily-report/",
    "permalink" => "/sideproject/trade/daily-report/#{date_str}-#{sess['suffix']}/",
    "tags" => ["trade", "daily-report", sess["tag"]],
    "report_date" => date_str,
    "source" => "trade_report",
    "auto_generated" => true
  }
end

pattern = File.join(daily_root, "**", "{morning,afternoon}.md")
sources = Dir.glob(pattern, File::FNM_CASEFOLD).sort
if sources.empty?
  warn "WARN: no source files under #{daily_root}"
  exit 0
end

written = 0
skipped = 0

sources.each do |src_path|
  rel = src_path.sub(%r{\A#{Regexp.escape(daily_root)}[/\\]?}, "")
  parts = rel.split(%r{[/\\]})
  next unless parts.length == 4

  year, month, day, filename = parts
  session_file = File.basename(filename, ".md")
  next unless config["sessions"].key?(session_file)

  date_str = TradeReportSync.date_from_parts(year, month, day)
  if since_date && Date.parse(date_str) < since_date
    skipped += 1
    next
  end

  sess = config["sessions"][session_file]
  out_name = "#{date_str}-#{sess['suffix']}.md"
  out_path = File.join(output_dir, out_name)

  body = File.read(src_path, encoding: "UTF-8")
  front_matter = build_front_matter(date_str, session_file, config, body)
  content = TradeReportSync.render_page(front_matter, body)
  result = TradeReportSync.write_if_changed(out_path, content, dry_run: options[:dry_run])

  if result == :written
    written += 1
  else
    skipped += 1
  end
end

if options[:update_config] && options[:remote_sha] && !options[:dry_run]
  config["last_synced_sha"] = options[:remote_sha]
  File.write(TradeReportSync::CONFIG_PATH, config.to_yaml, encoding: "UTF-8")
  puts "updated #{TradeReportSync::CONFIG_PATH} last_synced_sha=#{options[:remote_sha]}"
end

puts "done: written=#{written} skipped=#{skipped}"
