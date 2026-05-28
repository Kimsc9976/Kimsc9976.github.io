# 공통: 문제 폴더 최신 시각 (README git log → mtime fallback)
def problem_latest_time(problem_path)
  readme = File.join(problem_path, "README.md")

  if File.exist?(readme)
    dir = File.dirname(readme)
    ts = `cd "#{dir}" && git log -1 --format="%ct" -- "README.md" 2>/dev/null`.strip
    return Time.at(ts.to_i) if ts != "" && ts.to_i.positive?

    return File.mtime(readme)
  end

  File.mtime(problem_path)
end

def sort_problems_newest_first(dirs)
  dirs.sort_by { |p| problem_latest_time(p) }.reverse
end
