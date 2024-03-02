import os

def check_path_access(path):
    
    exists = os.path.exists(path)

    if exists:
       
        readable = os.access(path, os.R_OK)
        print(f"Readable: {readable}")

        writable = os.access(path, os.W_OK)
        print(f"Writable: {writable}")

        executable = os.access(path, os.X_OK)
        print(f"Executable: {executable}")
    else:
        print("Path does not exist")