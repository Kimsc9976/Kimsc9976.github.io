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


def safe_path(str)
  str
    .unicode_normalize(:nfkc)       # 유니코드 정규화
    .gsub(/\p{Space}+/, "-")        # 이상한 공백들 → -
    .gsub(/[^\w\-가-힣]/, "")       # 위험 문자 제거
    .gsub(/-+/, "-")
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
end

puts
puts "=== Final sidebar structure ==="
pp sidebar   # pretty print (Ruby 내장)

File.write("_data/sidebar.yml", sidebar.to_yaml)

puts
puts "sidebar.yml updated successfully!"
