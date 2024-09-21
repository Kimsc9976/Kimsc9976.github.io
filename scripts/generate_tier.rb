require 'fileutils'
require 'time'

# Ensure the _posts directory exists
def ensure_posts_directory_exists
  puts "Checking if _posts directory exists..."
  Dir.mkdir('_posts') unless Dir.exist?('_posts')
  puts "_posts directory checked/created."
end

# Generate posts for each problem based on problem folders
def generate_problem_posts
  modules_dir = 'modules'

  puts "Checking if modules directory exists..."
  if Dir.exist?(modules_dir)
    puts "Modules directory found. Iterating through directories..."

    # Iterate through each category (e.g., Algorithm, 프로그래머스, 백준)
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

                # Create a new .md file in the _posts folder
                # Filename should follow the format: YYYY-MM-DD-title.md
                post_title = problem_folder.gsub(/\s+/, '-').downcase
                post_date = Time.now.strftime('%Y-%m-%d')
                post_filename = "#{post_date}-#{post_title}.md"
                post_file_path = File.join('_posts', post_filename)

                File.open(post_file_path, 'w') do |file|
                  file.write("---\n")
                  file.write("layout: post\n")
                  file.write("title: \"#{problem_folder}\"\n")
                  file.write("date: #{post_date} 10:00:00 +0900\n")
                  file.write("categories: #{category} #{tier}\n")
                  file.write("permalink: /#{category.downcase}/#{tier.downcase}/#{post_title}/\n")
                  file.write("---\n\n")

                  # Write the content of README.md to the post
                  file.write(File.read(readme_path))

                  puts "Created-0-post for #{problem_folder} in #{tier} - #{category} at #{post_file_path}"
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

# Generate posts from problem folders
generate_problem_posts
