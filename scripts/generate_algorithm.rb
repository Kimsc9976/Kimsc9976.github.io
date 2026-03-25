require "fileutils"
require "unicode_normalize/tables"
require "uri"

BASE = "modules/Algorithm"
OUT_BASE = "_algorithm"
FileUtils.mkdir_p(OUT_BASE)

# 파일 시스템 경로용: 한글을 유지하되 특수문자만 제거
def safe_path(str)
  str
    .unicode_normalize(:nfkc)       # 유니코드 정규화
    .gsub(/\p{Space}+/, "-")        # 이상한 공백들 → -
    .gsub(/[^\w\-\p{Hangul}]/, "")  # 영문, 숫자, 하이픈, 한글만 유지
    .gsub(/-+/, "-")
    .gsub(/^-|-$/, "")              # 앞뒤 하이픈 제거
    .downcase
end

# URL 경로용: 한글을 URL 인코딩
def safe_url_path(str)
  URI.encode_www_form_component(safe_path(str))
end

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
    tier_name = File.basename(File.dirname(p))
    problem_name = File.basename(p)
    {
      "title" => problem_name,
      "url" => "/algorithm/#{safe_url_path(site_name)}/#{safe_url_path(tier_name)}/#{safe_url_path(problem_name)}/"
    }
  end

  {
    "site" => site_name,
    "site_safe" => safe_url_path(site_name),
    "tiers" => tier_names,
    "tiers_safe" => tier_names.map { |t| safe_url_path(t) },
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
  # 티어별 링크 추가 (URL 인코딩)
  tiers_html = site["tiers"].zip(site["tiers_safe"]).map do |t, t_safe|
    "<li><a href='/algorithm/#{site['site_safe']}/#{t_safe}/'>#{t}</a></li>"
  end.join("\n")
  
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