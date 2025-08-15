import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified python script, with arguments if provided, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the python script, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional list of any additional arguments provided for function call.",
                items = types.Schema(
                    type = types.Type.STRING
                )
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)
    
    if not absolute_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ['uv', 'run', absolute_path]
        if args:
            commands.extend(args)
        
        result = subprocess.run(
            commands,
            capture_output=True,
            cwd=abs_working_directory,
            timeout=30,
            text=True
        ) #input=None,
        
        output = []
        
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output) if output else "No output produced."
    except subprocess.CalledProcessError as e:
        return f"Error: executing Python file: {e}"