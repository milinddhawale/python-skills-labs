import os
import shutil

def move_files(target_map, base_directory):
    for file_path, folder in target_map.items():
        target_dir = os.path.join(base_directory, folder)
        file_name = os.path.basename(file_path)
        destination = os.path.join(target_dir, file_name)

        shutil.move(file_path, destination)
