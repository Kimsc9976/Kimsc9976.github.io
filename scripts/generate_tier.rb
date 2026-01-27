require "fileutils"

BASE = "modules/Algorithm"
OUT_BASE = "_algorithm"

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

  groups = problem_dirs.each_slice(20).to_a

  sections = groups.map.with_index do |slice, idx|
    links = slice.map do |p|
      name = File.basename(p)
      "<li><a href=\"./#{name}/\">#{name}</a></li>"
    end.join("\n")

    <<~HTML
    <h2>#{idx * 20 + 1} ~ #{idx * 20 + slice.size}</h2>
    <ul class="problem-grid collapsed">
    #{links}
    </ul>
    HTML
  end.join("\n")

  md = <<~MD
  ---
  layout: tier
  title: #{File.basename(relative)}
  platform: #{relative.split(File::SEPARATOR).first}
  permalink: /algorithm/#{relative}/
  ---

  #{sections}
  MD

  File.write("#{out_dir}/index.md", md)
  puts "  → index.md created in #{out_dir}"
end
