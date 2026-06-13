#!/usr/bin/env ruby
# frozen_string_literal: true

# modules/trade_report/journal/YYYY/MM/DD/{date}_journal.md
#   → sideproject/trade/journal/YYYY-MM-DD.md
# charts/*.png → assets/images/trade/journal/YYYY-MM-DD/*.png
# chart.png (있으면) → assets/images/trade/journal/YYYY-MM-DD-chart.png (헤더·front matter)

require "optparse"
require_relative "trade_report_sync_utils"

options = { dry_run: false, since: nil, source: nil }

OptionParser.new do |o|
  o.banner = "Usage: ruby scripts/sync_trade_journal.rb [options]"
  o.on("--source PATH", "trade_report 경로 (기본: modules/trade_report)") { |v| options[:source] = v }
  o.on("--since DATE",  "YYYY-MM-DD 이후만 처리")                         { |v| options[:since]  = v }
  o.on("--dry-run",     "파일을 쓰지 않고 변경 목록만 출력")              { options[:dry_run] = true }
end.parse!

source_root = File.expand_path(options[:source] || TradeReportSync::DEFAULT_SOURCE)
abort "ERROR: source not found: #{source_root}" unless Dir.exist?(source_root)

config           = TradeReportSync.load_config
journal_cfg      = config.fetch("journal")
journal_root     = File.join(source_root, journal_cfg["source_root"])
output_dir       = File.join(TradeReportSync::ROOT, journal_cfg["output_dir"])
chart_output_dir = File.join(TradeReportSync::ROOT, journal_cfg["chart_output_dir"])
charts_subdir    = journal_cfg.fetch("charts_subdir", "charts")
since_date       = TradeReportSync.parse_since(options[:since])

written = 0
skipped = 0

TradeReportSync.day_dirs(journal_root).each do |day_dir|
  year, month, day = TradeReportSync.parts_from_dir(day_dir, journal_root)
  next unless year && month && day

  date = TradeReportSync.date_str(year, month, day)
  next if since_date && Date.parse(date) < since_date

  payload = TradeReportSync.collect_journal_body(day_dir, date)
  unless payload
    warn "WARN: #{day_dir} — md 파일 없음, 건너뜀"
    next
  end

  TradeReportSync.sync_journal_charts(
    day_dir,
    chart_output_dir,
    date,
    charts_subdir: charts_subdir,
    dry_run: options[:dry_run]
  )

  body = TradeReportSync.rewrite_journal_chart_refs(payload[:body], date)

  date_field = if payload[:generated_at]
                 payload[:generated_at].strftime("%Y-%m-%d %H:%M:%S +0900")
               else
                 "#{date} #{journal_cfg['default_time']}"
               end

  chart_src      = File.join(day_dir, journal_cfg["chart_source_name"])
  chart_web_path = "/assets/images/trade/journal/#{date}-chart.png"
  chart_dest     = File.join(chart_output_dir, "#{date}-chart.png")

  chart_result = TradeReportSync.copy_if_changed(chart_src, chart_dest, dry_run: options[:dry_run])
  written += 1 if chart_result == :written

  prepend_header_chart = journal_cfg.fetch("prepend_header_chart", false)

  front_matter = {
    "layout"         => "sideproject",
    "title"          => "#{date} 매매일지",
    "project"        => "trade",
    "trade_section"  => "journal",
    "date"           => date_field,
    "parent_url"     => "/sideproject/trade/journal/",
    "permalink"      => "/sideproject/trade/journal/#{date}/",
    "tags"           => ["trade", "journal"],
    "journal_date"   => date,
    "source"         => "trade_report",
    "auto_generated" => true
  }

  if File.exist?(chart_src)
    front_matter["chart"] = chart_web_path
    if prepend_header_chart
      body = "## 📈 Buy / Sell 차트\n\n![#{date} 매매 차트](#{chart_web_path}){: .trade-chart}\n\n#{body.strip}"
    end
  end

  out_path = File.join(output_dir, "#{date}.md")
  content  = TradeReportSync.render_page(front_matter, body)
  result   = TradeReportSync.write_if_changed(out_path, content, dry_run: options[:dry_run])

  result == :written ? written += 1 : skipped += 1
end

puts "done: written=#{written} skipped=#{skipped}"
