require "open3"

# 경로가 속한 git 저장소(서브모듈 포함) 루트 탐색
def git_repo_root(path)
  dir = File.expand_path(path)
  loop do
    return dir if File.exist?(File.join(dir, ".git"))

    parent = File.dirname(dir)
    return nil if parent == dir

    dir = parent
  end
end

# 저장소별 README.md 최신 커밋 시각 맵 (git log 1회 호출, 셸 미사용)
def readme_commit_times(repo_root)
  @readme_commit_times ||= {}
  @readme_commit_times[repo_root] ||= begin
    out, status = Open3.capture2(
      "git", "-C", repo_root, "-c", "core.quotepath=off",
      "log", "--format=%x00%ct", "--name-only", "--", "*README.md"
    )
    times = {}
    if status.success?
      ts = nil
      out.force_encoding("UTF-8").each_line do |line|
        line = line.chomp
        if line.start_with?("\0")
          ts = line[1..].to_i
        elsif !line.empty? && ts
          times[File.expand_path(line, repo_root)] ||= Time.at(ts)
        end
      end
    end
    times
  rescue SystemCallError
    {}
  end
end

# 공통: 문제 폴더 최신 시각 (README git log → mtime fallback)
def problem_latest_time(problem_path)
  readme = File.join(problem_path, "README.md")

  if File.exist?(readme)
    root = git_repo_root(problem_path)
    time = root && readme_commit_times(root)[File.expand_path(readme)]
    return time if time

    return File.mtime(readme)
  end

  File.mtime(problem_path)
end

def sort_problems_newest_first(dirs)
  dirs.sort_by { |p| problem_latest_time(p) }.reverse
end
