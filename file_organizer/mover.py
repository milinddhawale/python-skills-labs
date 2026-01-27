import os
import shutil

def move_files(target_map, base_directory):
    """
    Move files to target folders based on organizer output.

    Args:
        target_map (dict): mapping of file path to target folder name
        base_directory (str): directory where target folder will be created.
    """
    for _, folder in target_map.items():
        target_dir = os.path.join(base_directory, folder)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

#This ensures - folders exist - no crash on first run