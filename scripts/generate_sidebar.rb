require "yaml"

BASE = "modules/Algorithm"
OUT_BASE = "algorithm"

puts "=== Sidebar Generator Debug Mode ==="
puts "BASE DIR: #{BASE}"
puts "Exists? #{Dir.exist?(BASE)}"
puts

sidebar = File.exist?("_data/sidebar.yml") ? YAML.load_file("_data/sidebar.yml") : {}
sidebar["algorithm"] ||= {}

Dir.glob("#{BASE}/*").each do |platform_dir|
  puts "Platform dir found: #{platform_dir}"

  unless File.directory?(platform_dir)
    puts "  -> Not a directory, skip"
    next
  end

  platform = File.basename(platform_dir)
  sidebar["algorithm"][platform] = []

  Dir.glob("#{platform_dir}/*").each do |tier_dir|
    puts "  Tier dir found: #{tier_dir}"

    unless File.directory?(tier_dir)
      puts "    -> Not a directory, skip"
      next
    end
    sidebar["algorithm"][platform] << File.basename(tier_dir)

  end
end

puts
puts "=== Final sidebar structure ==="
pp sidebar   # pretty print (Ruby 내장)

File.write("_data/sidebar.yml", sidebar.to_yaml)

puts
puts "sidebar.yml updated successfully!"
