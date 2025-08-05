import os
from .config import *

def get_file_content(working_directory, file_path):
    #make sure file is within working directory and is a file
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory = os.path.abspath(working_directory)
        
    if not absolute_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"' 
    
    file = open(absolute_path, "r")
    
            
    if os.path.getsize(absolute_path) > CHARACTER_LIMIT:
        return f'{file.read(CHARACTER_LIMIT)}\n [...File "{file_path}" truncated at 10000 characters]'
    return file.read()
        
            
            

    
    