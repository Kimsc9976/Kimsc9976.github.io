require 'yaml'

# modules 폴더의 첫 번째 레벨 디렉토리 구조 읽기
def read_directory_structure(dir)
  structure = {}

  Dir.foreach(dir) do |item|
    next if item == '.' or item == '..'
    path = File.join(dir, item)
    if File.directory?(path)
      structure[item] = path
    end
  end

  structure
end

# modules 폴더 구조 읽기
dir_structure = read_directory_structure('modules')

# YAML 파일로 저장
File.open('_data/sidebar_structure.yml', 'w') { |f| f.write(dir_structure.to_yaml) }
