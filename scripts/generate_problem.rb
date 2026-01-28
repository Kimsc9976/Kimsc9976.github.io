require "fileutils"
require "unicode_normalize/tables"
require "uri"

SRC = "modules/Algorithm"
OUT_BASE = "_algorithm"

LANG_MAP = {
  ".py"   => "python",
  ".cc"   => "cpp",
  ".java" => "java",
  ".sql"  => "sql",
  ".js"   => "javascript"
}

def preserved_date(md_path, source_path)
  if File.exist?(md_path)
    content = File.read(md_path)
    if content =~ /^date:\s*(.+)$/
      return $1.strip
    end
  end

  # 최초 생성일만 mtime 사용
  File.mtime(source_path).strftime("%Y-%m-%d %H:%M:%S")
end

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

Dir.glob("#{SRC}/*").each do |platform_dir|
  next unless File.directory?(platform_dir)
  platform_raw = File.basename(platform_dir)
  platform = safe_path(platform_raw)
  puts "#{platform_raw} -> #{platform}"

  Dir.glob("#{platform_dir}/*").each do |tier_dir|
    next unless File.directory?(tier_dir)
    tier_raw = File.basename(tier_dir)
    tier = safe_path(tier_raw)

    Dir.glob("#{tier_dir}/*").each do |problem|
      next unless File.directory?(problem)
      name_raw = File.basename(problem)
      name = safe_path(name_raw)

      out = File.join(OUT_BASE, platform, tier, name)
      FileUtils.mkdir_p(out)

      target = "#{out}/index.md"

      readme_path = "#{problem}/README.md"
      readme_content = File.exist?(readme_path) ? File.read(readme_path) : "_No description provided._"
      # puts "#{readme_path}"
      date = preserved_date(target, readme_path) # Readme.md 기준
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

      # permalink는 URL 인코딩된 경로 사용
      platform_url = safe_url_path(platform_raw)
      tier_url = safe_url_path(tier_raw)
      name_url = safe_url_path(name_raw)
      
      md = <<~MD
      ---
      layout: problem
      title: #{yaml_safe(name_raw)}
      platform: #{yaml_safe(platform_raw)}
      platform_url: #{yaml_safe(platform_url)}
      tier: #{yaml_safe(tier_raw)}
      tier_url: #{yaml_safe(tier_url)}
      permalink: #{yaml_safe("/algorithm/#{platform_url}/#{tier_url}/#{name_url}/")}
      date: #{yaml_safe(date)}
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