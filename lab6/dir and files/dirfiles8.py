import os

def delete_file_if_exists(file_path):

    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
                os.remove(file_path)