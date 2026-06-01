# frozen_string_literal: true

require "yaml"
require "fileutils"
require "digest"
require "time"
require "date"

module TradeReportSync
  ROOT = File.expand_path("..", __dir__)
  CONFIG_PATH = File.join(ROOT, "_data", "trade_report_sync.yml")
  DEFAULT_SOURCE = File.join(ROOT, "modules", "trade_report")

  module_function

  def load_config
    YAML.load_file(CONFIG_PATH)
  end

  def parse_generated_at(body)
    m = body.match(/>\s*생성\s*시각:\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})/)
    return nil unless m

    Time.strptime(m[1], "%Y-%m-%d %H:%M:%S")
  rescue ArgumentError
    nil
  end

  def render_page(front_matter, body)
    body = body.sub(/\A\s+/, "").sub(/\s+\z/, "")
    fm_yaml = front_matter.to_yaml.sub(/\A---\n/, "").sub(/\n\.\.\.\n\z/, "")
    "---\n#{fm_yaml}---\n\n#{body}\n"
  end

  def write_if_changed(out_path, content, dry_run:)
    digest = Digest::SHA256.hexdigest(content)
    if File.exist?(out_path) && Digest::SHA256.hexdigest(File.read(out_path, encoding: "UTF-8")) == digest
      return :skipped
    end

    if dry_run
      puts "[dry-run] would write #{out_path}"
    else
      FileUtils.mkdir_p(File.dirname(out_path))
      File.write(out_path, content, encoding: "UTF-8")
      puts "wrote #{out_path}"
    end
    :written
  end

  def copy_if_changed(src_path, dest_path, dry_run:)
    return :skipped unless File.exist?(src_path)

    if File.exist?(dest_path) &&
       Digest::SHA256.file(src_path).hexdigest == Digest::SHA256.file(dest_path).hexdigest
      return :skipped
    end

    if dry_run
      puts "[dry-run] would copy #{src_path} -> #{dest_path}"
    else
      FileUtils.mkdir_p(File.dirname(dest_path))
      FileUtils.cp(src_path, dest_path)
      puts "copied #{dest_path}"
    end
    :written
  end

  def parse_since(since)
    return nil if since.to_s.empty?

    Date.parse(since)
  rescue ArgumentError
    abort "ERROR: invalid --since date: #{since}"
  end

  def date_from_parts(year, month, day)
    format("%04d-%02d-%02d", year.to_i, month.to_i, day.to_i)
  end
end
