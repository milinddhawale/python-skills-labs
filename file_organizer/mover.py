import os
import shutil

def move_files(target_map, base_directory, dry_run=False):
    for file_path, folder in target_map.items():
        try:
           target_dir = os.path.join(base_directory, folder)
           file_name = os.path.basename(file_path)
           destination = os.path.join(target_dir, file_name)
           
           if dry_run:
               print(f"[DRY RUN] {file_path} -> {destination}")
               continue
           
           os.makedirs(target_dir, exist_ok=True)
           shutil.move(file_path, destination)
           print(f"Moved: {file_path} -> {destination}")

        except Exception as e:
            print(f"Failed to move {file_path}: {e}")
