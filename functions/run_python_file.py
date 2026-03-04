import subprocess
import os


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