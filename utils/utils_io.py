import os
import yaml
from docx.document import Document


# Load the YAML configuration
def load_config(config_file: str):
    if config_file.endswith('.yaml') or config_file.endswith('.yml'):
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
        return config
    else:
        raise ValueError("Invalid configuration file format. Use either '.yaml' or '.yml'.")


def check_create_save_directory(save_directory: str):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory, exist_ok=True)


def save_docx(docx_obj: Document, docx_save_file: str):
    if docx_save_file.endswith(".docx"):
        docx_obj.save(docx_save_file)
    else:
        raise ValueError(f"Invalid file format for saving the DOCX document. {docx_save_file} Use '.docx'.")


def remove_files_from_dir(directory: str, extension: str = ".docx"):
    """
    Removes all .docx files from the specified directory.
    """
    for file_name in os.listdir(directory):
        if file_name.endswith(extension):
            file_path = os.path.join(directory, file_name)
            try:
                os.remove(file_path)  # Remove the file
                print(f"Removed: {file_path}")
            except OSError as e:
                print(f"Error deleting file {file_path}: {e}")
