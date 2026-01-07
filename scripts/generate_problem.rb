require 'fileutils'

# Ensure the _posts directory exists
def ensure_posts_directory_exists
  puts "Checking if _posts directory exists..."
  Dir.mkdir('_posts') unless Dir.exist?('_posts')
  puts "_posts directory checked/created."
end

# Generate pages for each problem based on problem folders
def generate_problem_pages
  modules_dir = 'modules'

  puts "Checking if modules directory exists..."
  if Dir.exist?(modules_dir)
    puts "Modules directory found. Iterating through directories..."

    # Iterate through each category (e.g., SWEA, 백준)
    Dir.entries(modules_dir).each do |category|
      next if category == '.' || category == '..'

      category_path = File.join(modules_dir, category)
      if Dir.exist?(category_path)
        # Iterate through each tier (e.g., Bronze, Gold, Silver)
        Dir.entries(category_path).each do |tier|
          next if tier == '.' || tier == '..'

          tier_path = File.join(category_path, tier)
          if Dir.exist?(tier_path)
            # Iterate through each problem folder within the tier
            Dir.entries(tier_path).each do |problem_folder|
              next if problem_folder == '.' || problem_folder == '..'

              problem_path = File.join(tier_path, problem_folder)
              if Dir.exist?(problem_path)
                # Skip if directory is empty or only contains .git files (submodule not checked out)
                entries = Dir.entries(problem_path).reject { |e| e == '.' || e == '..' || e == '.git' }
                if entries.empty?
                  puts "Skipping empty directory: #{problem_path}"
                  next
                end

                # Find the README.md file within the problem folder
                readme_path = File.join(problem_path, 'README.md')
                code_files = Dir.entries(problem_path).select do |file|
                  file != '.' && file != '..' && file != '.git' && 
                  %w(.py .java .cpp .js .ts .c .cs).include?(File.extname(file))
                end
                
                # Create an index.md file for the problem
                index_file_path = File.join(problem_path, 'index.md')
                begin
                  File.open(index_file_path, 'w') do |file|
                    file.write("---\n")
                    file.write("layout: default\n")
                    file.write("title: \"#{problem_folder}\"\n")
                    file.write("permalink: /#{category.downcase}/#{tier.downcase}/#{problem_folder.downcase}/\n")
                    file.write("---\n")

                    # Write the content of README.md to the index.md
                    if File.exist?(readme_path)
                      file.write(File.read(readme_path))
                    end

                    # Include code files as code blocks
                    code_files.each do |code_file|
                      code_file_path = File.join(problem_path, code_file)
                      if File.exist?(code_file_path)
                        file.write("\n## #{File.basename(code_file)}\n")
                        file.write("```#{File.extname(code_file).delete('.')}\n")
                        file.write(File.read(code_file_path))
                        file.write("\n```\n")
                      end
                    end
                  end
                  puts "Created page for #{problem_folder} in #{tier} - #{category} at #{index_file_path}"
                rescue => e
                  puts "Error creating page for #{problem_folder}: #{e.message}"
                end
              end
            end
          end
        end
      end
    end
  else
    puts "Modules directory not found!"
  end
end

# Ensure the _posts directory exists
ensure_posts_directory_exists

# Generate pages from problem folders
generate_problem_pages
