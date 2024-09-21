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
                # Find the README.md file within the problem folder
                readme_path = File.join(problem_path, 'README.md')
                if File.exist?(readme_path)
                  # Create an index.md file for the problem
                  index_file_path = File.join(problem_path, 'index.md')
                  File.open(index_file_path, 'w') do |file|
                    file.write("---\n")
                    file.write("layout: default\n")
                    file.write("title: \"#{problem_folder}\"\n")
                    file.write("permalink: /#{category.downcase}/#{tier.downcase}/#{problem_folder.downcase}/\n")
                    file.write("---\n")
                    
                    # Write the content of README.md to the index.md
                    file.write(File.read(readme_path))
                  end
                  puts "Created page for #{problem_folder} in #{tier} - #{category} at #{index_file_path}"
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
