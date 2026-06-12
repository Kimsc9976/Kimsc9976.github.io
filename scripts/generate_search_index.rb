require "json"
require "fileutils"
require "unicode_normalize/tables"
require "uri"

SRC = "modules/Algorithm"
OUT = "assets/search-index.json"

def safe_path(str)
  str
    .unicode_normalize(:nfkc)
    .gsub(/\p{Space}+/, "-")
    .gsub(/[^\w\-\p{Hangul}]/, "")
    .gsub(/-+/, "-")
    .gsub(/^-|-$/, "")
    .downcase
end

def safe_url_path(str)
  URI.encode_www_form_component(safe_path(str))
end

def parse_problem_name(name_raw)
  normalized = name_raw.unicode_normalize(:nfkc).strip

  if normalized =~ /^(\d+)\.\s*(.+)$/
    {
      "problem_id" => Regexp.last_match(1),
      "title_clean" => Regexp.last_match(2).strip,
      "title" => normalized
    }
  else
    {
      "problem_id" => "",
      "title_clean" => normalized,
      "title" => normalized
    }
  end
end

entries = []

Dir.glob("#{SRC}/*").each do |platform_dir|
  next unless File.directory?(platform_dir)

  platform_raw = File.basename(platform_dir)
  platform_url = safe_url_path(platform_raw)

  Dir.glob("#{platform_dir}/*").each do |tier_dir|
    next unless File.directory?(tier_dir)

    tier_raw = File.basename(tier_dir)
    tier_url = safe_url_path(tier_raw)

    Dir.glob("#{tier_dir}/*").each do |problem_dir|
      next unless File.directory?(problem_dir)

      name_raw = File.basename(problem_dir)
      parsed = parse_problem_name(name_raw)
      name_url = safe_url_path(name_raw)

      entries << {
        "title" => parsed["title"],
        "title_clean" => parsed["title_clean"],
        "problem_id" => parsed["problem_id"],
        "platform" => platform_raw,
        "tier" => tier_raw,
        "url" => "/algorithm/#{platform_url}/#{tier_url}/#{name_url}/"
      }
    end
  end
end

entries.sort_by! { |entry| [entry["platform"], entry["tier"], entry["title"]] }

FileUtils.mkdir_p(File.dirname(OUT))
File.write(OUT, JSON.pretty_generate(entries))

puts "✅ Search index generated (#{entries.size} problems) → #{OUT}"
