import os

def get_files_info(working_directory, directory="."):
    absolute_path = os.path.abspath(os.path.join(working_directory, directory))
    working_directory = os.path.abspath(working_directory)
    
    if not absolute_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory\n'
    try:
        files_info = []
        #loop to build string for file info output
        for item in os.listdir(absolute_path):
            if not item.startswith("__"):
                item_path = os.path.join(absolute_path, item)
                is_dir = os.path.isdir(item_path)
                file_size = os.path.getsize(item_path)
                files_info.append(f'- {item}: file_size={file_size} bytes, is_dir={is_dir}')
            
        return '\n'.join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"