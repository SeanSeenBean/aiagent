from functions.config import WORKING_DIRECTORY
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def call_function(function_call_part, verbose = False):
    available_functions = {
        "get_files_info" : get_files_info,
        "get_file_content" : get_file_content,
        "write_file" : write_file,
        "run_python_file" : run_python_file
    }
    function_name = function_call_part.name
    args = function_call_part.args
    args["working_directory"] = WORKING_DIRECTORY
    
    try:
        
        if verbose:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        else:
            print(f" - Calling function: {function_call_part.name}")
        if function_name not in available_functions:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )
        if function_name not in available_functions:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )
        
        function_result = available_functions[function_call_part.name](**function_call_part.args) 
        
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result},
                )
            ],
        )
    
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Error calling function: {function_name} \nError: {e}"},
                )
            ],
        )
        