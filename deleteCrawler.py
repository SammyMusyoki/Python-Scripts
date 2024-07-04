import os
import shutil

def delete_dir(path):
    try:
        shutil.rmtree(path)
        print(f"Deleted: {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")

def scan_and_delete(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for dir_name in dirs:
            if dir_name == "node_modules" or dir_name == "venv":
                dir_path = os.path.join(root, dir_name)
                delete_dir(dir_path)

if __name__ == "__main__":
    root_folder = r"path/to/your/projects/directory"
    scan_and_delete(root_folder)

# Exited in 1623.956 seconds
