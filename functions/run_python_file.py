import subprocess
import os
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_directory = os.path.abspath(working_directory)

        full_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        valid_target_dir = os.path.commonpath([abs_working_directory, full_path]) == abs_working_directory
        if not valid_target_dir:
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not file_path.endswith(".py"):
            raise Exception(f'Error: "{file_path}" is not a Python file')
        if not os.path.isfile(full_path):
            raise Exception(f'Error: "{file_path}" does not exist')
        
        command = ["python", full_path].extend(args) if args else ["python", full_path]

        completedProcess = subprocess.run(command, cwd=abs_working_directory, timeout=30 , capture_output=True, text=True)
        outputString = ""
        if completedProcess.returncode != 0:
            outputString += f'Process exited with code {completedProcess.returncode}\n'
        if not completedProcess.stdout and not completedProcess.stderr:
            outputString += 'No output produced.'
        else:
            if completedProcess.stdout:
                outputString += f'STDOUT:\n{completedProcess.stdout}\n'
            if completedProcess.stderr:
                outputString += f'STDERR:\n{completedProcess.stderr}\n'
        return outputString.strip()
    
    except Exception as e:
        return f'Error executing "{file_path}": {str(e)}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified Python file relative to the working directory, optionally with arguments, and returns the output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional arguments to pass to the Python file",
            ),
        },
    ),
)