import os

def list_directories(path):

    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_directories_files(path):
   
    directories_files = os.listdir(path)
    return directories_files
