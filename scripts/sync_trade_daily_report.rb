#!/usr/bin/env ruby
# frozen_string_literal: true

# modules/trade_report/daily-report/YYYY/MM/DD/morning.md   → sideproject/trade/daily-report/YYYY-MM-DD-am.md
# modules/trade_report/daily-report/YYYY/MM/DD/afternoon.md → sideproject/trade/daily-report/YYYY-MM-DD-pm.md
#
# 오전/오후를 반드시 분리된 파일로 생성합니다.

require "optparse"
require_relative "trade_report_sync_utils"

SESSION_MAP = {
  "morning"   => { suffix: "am", label: "오전", time: "09:00:00 +0900", tag: "오전" },
  "afternoon" => { suffix: "pm", label: "오후", time: "15:30:00 +0900", tag: "오후" }
}.freeze

options = { dry_run: false, since: nil, source: nil, update_config: false, remote_sha: nil }

OptionParser.new do |o|
  o.banner = "Usage: ruby scripts/sync_trade_daily_report.rb [options]"
  o.on("--source PATH", "trade_report 경로 (기본: modules/trade_report)") { |v| options[:source] = v }
  o.on("--since DATE",  "YYYY-MM-DD 이후만 처리")                         { |v| options[:since]  = v }
  o.on("--dry-run",     "파일을 쓰지 않고 변경 목록만 출력")              { options[:dry_run] = true }
  o.on("--update-config", "last_synced_sha 갱신")                        { options[:update_config] = true }
  o.on("--remote-sha SHA", "기록할 원격 SHA")                             { |v| options[:remote_sha] = v }
end.parse!

source_root = File.expand_path(options[:source] || TradeReportSync::DEFAULT_SOURCE)
abort "ERROR: source not found: #{source_root}" unless Dir.exist?(source_root)

config     = TradeReportSync.load_config
dr_root    = File.join(source_root, config["source_root"])           # .../daily-report
output_dir = File.join(TradeReportSync::ROOT, config["output_dir"]) # sideproject/trade/daily-report
since_date = TradeReportSync.parse_since(options[:since])

FileUtils.mkdir_p(output_dir) unless options[:dry_run]

written = 0
skipped = 0

TradeReportSync.day_dirs(dr_root).each do |day_dir|
  year, month, day = TradeReportSync.parts_from_dir(day_dir, dr_root)
  next unless year && month && day

  date = TradeReportSync.date_str(year, month, day)
  next if since_date && Date.parse(date) < since_date

  SESSION_MAP.each do |filename, sess|
    src = File.join(day_dir, "#{filename}.md")
    next unless File.exist?(src)

    body = File.read(src, encoding: "UTF-8")

    generated = TradeReportSync.parse_generated_at(body)
    date_field = generated ? generated.strftime("%Y-%m-%d %H:%M:%S +0900") : "#{date} #{sess[:time]}"

    front_matter = {
      "layout"        => "sideproject",
      "title"         => "#{date} 일간 레포트 (#{sess[:label]})",
      "project"       => "trade",
      "trade_section" => "daily-report",
      "session"       => sess[:suffix],
      "session_label" => sess[:label],
      "date"          => date_field,
      "parent_url"    => "/sideproject/trade/daily-report/",
      "permalink"     => "/sideproject/trade/daily-report/#{date}-#{sess[:suffix]}/",
      "tags"          => ["trade", "daily-report", sess[:tag]],
      "report_date"   => date,
      "source"        => "trade_report",
      "auto_generated" => true
    }

    out_path = File.join(output_dir, "#{date}-#{sess[:suffix]}.md")
    content  = TradeReportSync.render_page(front_matter, body)
    result   = TradeReportSync.write_if_changed(out_path, content, dry_run: options[:dry_run])

    result == :written ? written += 1 : skipped += 1
  end
end

if options[:update_config] && options[:remote_sha] && !options[:dry_run]
  config["last_synced_sha"] = options[:remote_sha]
  File.write(TradeReportSync::CONFIG_PATH, config.to_yaml, encoding: "UTF-8")
  puts "config   #{TradeReportSync::CONFIG_PATH} last_synced_sha=#{options[:remote_sha]}"
end

puts "done: written=#{written} skipped=#{skipped}"
