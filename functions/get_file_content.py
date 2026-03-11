import os

from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path="."):
    try:
        abs_working_directory = os.path.abspath(working_directory)

        full_path = os.path.normpath(os.path.join(abs_working_directory, file_path))

        valid_target_dir = os.path.commonpath([abs_working_directory, full_path]) == abs_working_directory
        if not valid_target_dir:
            raise Exception(f'Error: Cannot list "{full_path}" as it is outside the permitted working directory')
        if not os.path.isfile(full_path):
            raise Exception(f'Error: File not found or is not a regular file: "{full_path}"')
        

        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{os.path.basename(full_path)}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    
    except Exception as e:
        return f'Error: {str(e)}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a specified file relative to the working directory, up to a maximum number of characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to get content from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)