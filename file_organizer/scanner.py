import os

def scan_directory(directory_path):
    items = []

    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)

        item_info = {
            "name": entry,
            "path": full_path
        }
        
        items.append(item_info)

    return items
