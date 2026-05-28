require "fileutils"
require "unicode_normalize/tables"
require "uri"
require_relative "algorithm_utils"

BASE = "modules/Algorithm"
OUT_BASE = "_algorithm"

puts "BASE exists? #{Dir.exist?(BASE)}"

# 파일 시스템 경로용: 한글을 유지하되 특수문자만 제거
def safe_path(str)
  str
    .unicode_normalize(:nfkc)       # 유니코드 정규화
    .gsub(/\p{Space}+/, "-")        # 이상한 공백들 → -
    .gsub(/[^\w\-가-힣]/, "")       # 위험 문자 제거
    .gsub(/-+/, "-")
    .gsub(/^-|-$/, "")              # 앞뒤 하이픈 제거
    .downcase
end

# URL 경로용: 한글을 URL 인코딩
def safe_url_path(str)
  URI.encode_www_form_component(safe_path(str))
end

# YAML-safe 문자열: 특수 문자를 이스케이프
def yaml_safe(str)
  return '""' if str.nil? || str.empty?
  str_str = str.to_s
  # YAML에서 따옴표가 필요할 수 있는 문자들 체크
  # % 문자는 URL 인코딩에 사용되므로 항상 따옴표 필요
  if str_str =~ /[:%\[\]{}|&*!@#`>\\]|^\s|\s$|^\d+\.\s/
    # 따옴표로 감싸고 내부 따옴표와 백슬래시는 이스케이프
    "\"#{str_str.gsub('\\', '\\\\').gsub('"', '\\"')}\""
  else
    str_str
  end
end

Dir.glob("#{BASE}/*/*").each do |tier_path|
  next unless File.directory?(tier_path)

  # BASE 이후 상대경로 추출 → 백준/Bronze
  relative_raw = tier_path.sub("#{BASE}/", "")
  relative_parts = relative_raw.split(File::SEPARATOR)
  relative = relative_parts.map { |p| safe_path(p) }.join(File::SEPARATOR)

  puts "Tier found: #{relative_raw} -> #{relative}"

  out_dir = File.join(OUT_BASE, relative)
  FileUtils.mkdir_p(out_dir)

  problem_dirs = Dir.glob("#{tier_path}/*").select { |p| File.directory?(p) }
  next if problem_dirs.empty?

  problem_dirs = sort_problems_newest_first(problem_dirs)

  groups = problem_dirs.each_slice(20).to_a

  sections = groups.map.with_index do |slice, idx|
    links = slice.map do |p|
      name = File.basename(p)
      safe_url = safe_url_path(name)
      "<li><a href=\"./#{safe_url}/\">#{name}</a></li>"
    end.join("\n")

    <<~HTML
    <h2>#{idx * 20 + 1} ~ #{idx * 20 + slice.size}</h2>
    <ul class="problem-grid collapsed">
    #{links}
    </ul>
    HTML
  end.join("\n")

  # permalink는 URL 인코딩된 경로 사용
  relative_url = relative_parts.map { |p| safe_url_path(p) }.join("/")
  
  platform_raw = relative_parts.first
  platform_url = safe_url_path(platform_raw)
  tier_raw = relative_parts[1] || File.basename(relative_raw)
  tier_url = safe_url_path(tier_raw)
  
  md = <<~MD
  ---
  layout: tier
  title: #{yaml_safe(File.basename(relative_raw))}
  platform: #{yaml_safe(platform_raw)}
  platform_url: #{yaml_safe(platform_url)}
  tier: #{yaml_safe(tier_raw)}
  tier_url: #{yaml_safe(tier_url)}
  permalink: #{yaml_safe("/algorithm/#{relative_url}/")}
  ---

  #{sections}
  MD

  File.write("#{out_dir}/index.md", md)
  puts "  → index.md created in #{out_dir}"
end
