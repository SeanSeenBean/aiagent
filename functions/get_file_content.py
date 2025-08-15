import os
from .config import CHARACTER_LIMIT
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read's content of the specified file and then returns the contents of the file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to be read, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    #make sure file is within working directory and is a file
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_directory = os.path.abspath(working_directory)
        
    if not absolute_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
    if not os.path.isfile(absolute_path):
            return f'Error: File not found or is not a regular file: "{file_path}"' 
        
    try: 
        with open(absolute_path, "r") as file:
            content = file.read(CHARACTER_LIMIT)
            if os.path.getsize(absolute_path) > CHARACTER_LIMIT:
                content += f'\n[...File "{file_path}" truncated at 10000 characters]'
        return content 
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
        
            
            

    
    