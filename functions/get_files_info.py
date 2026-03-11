import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        abs_working_directory = os.path.abspath(working_directory)

        full_path = os.path.normpath(os.path.join(abs_working_directory, directory))

        valid_target_dir = os.path.commonpath([abs_working_directory, full_path]) == abs_working_directory
        if not valid_target_dir:
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(full_path):
            raise Exception(f'Error: "{directory}" is not a directory')
        
        items_info = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            item_size = os.path.getsize(item_path)
            is_directory = os.path.isdir(item_path)
            items_info.append(f'- {item}: file_size={item_size} bytes, is_dir={is_directory}')

        return '\n'.join(items_info)
    except Exception as e:
        return f'Error: {str(e)}'
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)