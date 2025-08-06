import os

def write_file(working_directory, file_path, content):
    #checks if file_path is within the working_directory
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory = os.path.abspath(working_directory)
        
    if not absolute_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_path):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
            
    #check for file existance, create 
    try:        
        with open(file_path, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Error writing file "{file_path}": {e}'