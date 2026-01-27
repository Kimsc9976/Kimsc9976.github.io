require "fileutils"

SRC = "modules/Algorithm"
OUT_BASE = "_algorithm"

LANG_MAP = {
  ".py"   => "python",
  ".cc"   => "cpp",
  ".java" => "java",
  ".sql"  => "sql",
  ".js"   => "javascript"
}

Dir.glob("#{SRC}/*").each do |platform_dir|
  next unless File.directory?(platform_dir)
  platform = File.basename(platform_dir)
  puts "#{platform}"

  Dir.glob("#{platform_dir}/*").each do |tier_dir|
    next unless File.directory?(tier_dir)
    tier = File.basename(tier_dir)

    Dir.glob("#{tier_dir}/*").each do |problem|
      next unless File.directory?(problem)
      name = File.basename(problem)

      out = File.join(OUT_BASE, platform, tier, name)
      FileUtils.mkdir_p(out)

      target = "#{out}/index.md"

      readme_path = "#{problem}/README.md"
      readme_content = File.exist?(readme_path) ? File.read(readme_path) : "_No description provided._"
      date = File.mtime(readme_path).iso8601 # 2026-01-28T14:33:22+09:00
      code_blocks = []

      LANG_MAP.each do |ext, lang|
        Dir.glob("#{problem}/*#{ext}").each do |file|
          content = File.read(file)

          code_blocks << <<~CODE
          ### 📄 #{File.basename(file)}

          ```#{lang}
          #{content}
          ```
          CODE
        end
      end

      md = <<~MD
      ---
      layout: problem
      title: #{name}
      platform: #{platform}
      tier: #{tier}
      permalink: /algorithm/#{platform}/#{tier}/#{name}/
      date: #{date}
      ---

      #{readme_content}

      ## 💡 Solutions

      #{code_blocks.join("\n")}
      MD

      File.write(target, md)
    end
  end
end

puts "✅ All markdown pages generated safely (no Liquid includes)"