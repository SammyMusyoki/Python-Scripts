import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def delete_directory(path):
    try:
        shutil.rmtree(path)
        print(f"Deleted: {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")


def scan_and_delete(root_folder):
    directories_to_delete = []

    for root, dirs, files in os.walk(root_folder):
        for dir_name in dirs:
            if dir_name == 'node_modules' or dir_name == 'venv':
                dir_path = os.path.join(root, dir_name)
                directories_to_delete.append(dir_path)

    return directories_to_delete


def main(root_folder):
    start_time = time.time()

    directories_to_delete = scan_and_delete(root_folder)

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        future_to_dir = {executor.submit(
            delete_directory, dir_path): dir_path for dir_path in directories_to_delete}

        for future in as_completed(future_to_dir):
            dir_path = future_to_dir[future]
            try:
                future.result()
            except Exception as exc:
                print(f"Error deleting {dir_path}: {exc}")

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    # Set the root folder where your projects are located
    root_folder = r"path/to/your/projects/directory"
    main(root_folder)
