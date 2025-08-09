import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)
    
    if not absolute_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
        
    # Use the subprocess.run function to execute the Python file and get back a "completed_process" object. Make sure to:
    #     Set a timeout of 30 seconds to prevent infinite execution
    #     Capture both stdout and stderr
    #     Set the working directory properly
    #     Pass along the additional args if provided    
    # Return a string with the output formatted to include:    
    #     The stdout prefixed with STDOUT:, and stderr prefixed with STDERR:. The "completed_process" object has a stdout and stderr attribute.
    #     If the process exits with a non-zero code, include "Process exited with code X"
    #     If no output is produced, return "No output produced."
    
    # If any exceptions occur during execution, catch them and return an error string: 
    # print(f'file path: {file_path}')
    # print(f'absolute file path {absolute_path}')
    # print(f'working directory: {working_directory}')
    # print (f'absolute working directory: {abs_working_directory}')
    
    try:
        result = subprocess.run(
            (['uv', 'run', absolute_path] + args),
            capture_output=True,
            cwd=os.path.dirname(abs_working_directory),
            timeout=30,
            text=True
        ) #input=None,
       
    except subprocess.CalledProcessError as e:
        return f"Error: executing Python file: {e}"
    formatted_output = f"STDOUT: {result.stdout}\n STDERR: {result.stderr}"
    if result.returncode != 0:
        return (formatted_output + f'\nProcess exited with code {result.returncode}' )
    if len(result.stdout) == 0:
        return "No output produced"
    
    
    return  formatted_output