import os

def get_files_info(working_directory, directory="."):
    absolute_path = os.path.abspath(os.path.join(working_directory, directory))
    working_directory = os.path.abspath(working_directory)
    
    if not absolute_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
    elif not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory\n'
        
    directory_contents = os.listdir(absolute_path)
    files_info = ''
    #loop to build string for file info output
    for item in directory_contents:
        if not item.startswith("__"):
            item_path = os.path.join(absolute_path, item)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path)
            files_info += f'- {item}: file_size={file_size} bytes, is_dir={is_dir} \n'
            
    return files_info