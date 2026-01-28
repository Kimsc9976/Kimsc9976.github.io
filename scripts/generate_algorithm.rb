require "fileutils"

BASE = "modules/Algorithm"
OUT_BASE = "_algorithm"
FileUtils.mkdir_p(OUT_BASE)

# 각 사이트별 Tier 정보 수집
sites = Dir.glob("#{BASE}/*").select { |d| File.directory?(d) }

site_data = sites.map do |site_path|
  site_name = File.basename(site_path)

  tiers = Dir.glob("#{site_path}/*").select { |d| File.directory?(d) }
  # 티어 이름만
  tier_names = tiers.map { |t| File.basename(t) }
  puts "#{tier_names}"

  # 최근 문제 3개
  recent_problems = tiers.flat_map do |tier|
    Dir.glob("#{tier}/*").select { |p| File.directory?(p) }
  end.sort_by { |p| File.mtime(p) }.reverse.first(3).map do |p|
    {
      "title" => File.basename(p),
      "url" => "/algorithm/#{site_name}/#{File.basename(File.dirname(p))}/#{File.basename(p)}/"
    }
  end

  {
    "site" => site_name,
    "tiers" => tier_names,
    "recent" => recent_problems
  }
end

md = <<~MD
---
layout: algorithm
title: Algorithm Sites
permalink: /algorithm/
---

<div class="algorithm-grid">
#{site_data.map do |site|
  # 티어별 링크 추가
  tiers_html = site["tiers"].map { |t| "<li><a href='/algorithm/#{site['site']}/#{t}/'>#{t}</a></li>" }.join("\n")
  
  # 최근 문제 리스트 (문제만, 최신 순)
  recent_html = site["recent"].map { |p| "<li><a href='#{p['url']}'>#{p['title']}</a></li>" }.join("\n")

  <<~CARD
  <div class="algo-card">
    <h2>#{site['site']}</h2>

    <h3>Tiers</h3>
    <ul>#{tiers_html}</ul>

    <h3>Recent Problems</h3>
    <ul>#{recent_html}</ul>
  </div>
  CARD
end.join("\n")}
</div>
MD

File.write("#{OUT_BASE}/index.md", md)
puts "index.md created in #{OUT_BASE}"