import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes provided content to a specified file, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to be written to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the specified file.",
            ),
        },
    ),
)

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