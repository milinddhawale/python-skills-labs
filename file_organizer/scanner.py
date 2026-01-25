import os

def scan_directory(directory_path):
    items = []

    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        items.append(full_path)
        
    return items
