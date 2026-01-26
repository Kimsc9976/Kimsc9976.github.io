require "fileutils"

BASE = "modules/Algorithm"
OUT_BASE = "algorithm"

puts "BASE exists? #{Dir.exist?(BASE)}"

Dir.glob("#{BASE}/*/*").each do |tier_path|
  next unless File.directory?(tier_path)

  # BASE 이후 상대경로 추출 → 백준/Bronze
  relative = tier_path.sub("#{BASE}/", "")

  puts "Tier found: #{relative}"

  out_dir = File.join(OUT_BASE, relative)
  FileUtils.mkdir_p(out_dir)

  problem_dirs = Dir.glob("#{tier_path}/*").select { |p| File.directory?(p) }
  next if problem_dirs.empty?

  links = problem_dirs.map do |p|
    name = File.basename(p)
    "- [#{name}](./#{name}/)"
  end.join("\n")

  md = <<~MD
  ---
  layout: tier
  title: #{File.basename(relative)}
  permalink: /algorithm/#{relative}/
  ---

  #{links}
  MD

  File.write("#{out_dir}/index.md", md)
  puts "  → index.md created in #{out_dir}"
end
