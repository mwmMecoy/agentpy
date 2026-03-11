import os

from config import MAX_CHARS
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abs_working_directory = os.path.abspath(working_directory)

        full_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        valid_target_dir = os.path.commonpath([abs_working_directory, full_path]) == abs_working_directory
        if not valid_target_dir:
            raise Exception(f'Error: Cannot write to "{full_path}" as it is outside the permitted working directory')
        if  os.path.isdir(full_path):
            raise Exception(f'Error: Cannot write to "{file_path}" as it is a directory')
        
        # Make sure that all parent directories of the file_path exist. You can use os.makedirs() with the exist_ok=True argument to create any missing directories. If the necessary directory structure already exists, this will do nothing – which is what we want.
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        # Open the file at file_path in write mode ("w") and overwrite its contents with the content argument.
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {str(e)}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write content to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
    ),
)