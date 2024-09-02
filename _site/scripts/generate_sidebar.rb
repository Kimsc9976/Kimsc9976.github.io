require 'yaml'

# Ensure the _data directory exists
def ensure_data_directory_exists
  puts "Checking if _data directory exists..."
  Dir.mkdir('_data') unless Dir.exist?('_data')
  puts "_data directory checked/created."
end

# Generate sidebar structure based on modules directory
def generate_sidebar_structure
  sidebar_structure = {}

  # Define the base directory for modules
  modules_dir = 'modules'

  puts "Checking if modules directory exists..."
  # Ensure modules directory exists
  if Dir.exist?(modules_dir)
    puts "Modules directory found. Iterating through directories..."
    # Iterate through directories within the modules directory
    Dir.entries(modules_dir).each do |entry|
      next if entry == '.' || entry == '..'
      
      # For each directory, add an entry to the sidebar_structure
      sidebar_structure[entry] = Dir.entries(File.join(modules_dir, entry)).select do |file|
        File.directory?(File.join(modules_dir, entry, file)) && !(file == '.' || file == '..')
      end
    end
    puts "Sidebar structure generated: #{sidebar_structure}"
  else
    puts "Modules directory not found!"
  end

  # Write the structure to the YAML file
  puts "Writing to _data/sidebar_structure.yml..."
  File.open('_data/sidebar_structure.yml', 'w') do |file|
    file.write(sidebar_structure.to_yaml)
  end
  puts "sidebar_structure.yml file written."
end

# Ensure the _data directory exists
ensure_data_directory_exists

# Generate the sidebar structure
generate_sidebar_structure
