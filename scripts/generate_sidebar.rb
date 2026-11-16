require "yaml"
require "unicode_normalize/tables"

BASE = "modules/Algorithm"
OUT_BASE = "_algorithm"

puts "=== Sidebar Generator Debug Mode ==="
puts "BASE DIR: #{BASE}"
puts "Exists? #{Dir.exist?(BASE)}"
puts

sidebar = File.exist?("_data/sidebar.yml") ? YAML.load_file("_data/sidebar.yml") : {}
sidebar["algorithm"] ||= {}

# 티어 표시 순서 (Bronze → Silver → Gold → Platinum → Diamond ...)
# Dir.glob 순서는 OS·파일시스템마다 달라 그대로 쓰면 sidebar 순서가 섞임
TIER_ORDER = File.exist?("_data/tier_order.yml") ? YAML.load_file("_data/tier_order.yml").map { |t| t.to_s.downcase } : []

def tier_sort_key(tier)
  idx = TIER_ORDER.index(tier.to_s.downcase)
  idx ? [0, idx, ""] : [1, 0, tier.to_s] # 목록에 없는 티어는 뒤로, 이름순
end


def safe_path(str)
  str
    .unicode_normalize(:nfkc)       # 유니코드 정규화
    .gsub(/\p{Space}+/, "-")        # 이상한 공백들 → -
    .gsub(/[^\w\-가-힣]/, "")       # 위험 문자 제거
    .gsub(/-+/, "-")
    .gsub(/^-|-$/, "")              # 앞뒤 하이픈 제거
    .downcase
end

Dir.glob("#{BASE}/*").each do |platform_dir|
  puts "Platform dir found: #{platform_dir}"

  unless File.directory?(platform_dir)
    puts "  -> Not a directory, skip"
    next
  end

  platform_raw = File.basename(platform_dir)
  platform = safe_path(platform_raw)
  sidebar["algorithm"][platform] = []

  Dir.glob("#{platform_dir}/*").each do |tier_dir|
    puts "  Tier dir found: #{tier_dir}"

    unless File.directory?(tier_dir)
      puts "    -> Not a directory, skip"
      next
    end
    tier_raw = File.basename(tier_dir)
    tier = safe_path(tier_raw)
    sidebar["algorithm"][platform] << tier

  end

  sidebar["algorithm"][platform].sort_by! { |t| tier_sort_key(t) }
end

puts
puts "=== Final sidebar structure ==="
pp sidebar   # pretty print (Ruby 내장)

File.write("_data/sidebar.yml", sidebar.to_yaml)

puts
puts "sidebar.yml updated successfully!"
