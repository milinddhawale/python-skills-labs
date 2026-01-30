import os
import shutil

def move_files(target_map, base_directory):
    for file_path, folder in target_map.items():
        try:
           target_dir = os.path.join(base_directory, folder)
           
           os.makedirs(target_dir, exist_ok=True)

           file_name = os.path.basename(file_path)
           destination = os.path.join(target_dir, file_name)

           shutil.move(file_path, destination)
           print(f"Moved: {file_path} -> {destination}")

        except Exception as e:
            print(f"Failed to move {file_path}: {e}")
