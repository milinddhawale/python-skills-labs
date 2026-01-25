import os

def scan_directory(directory_path):
    items = []

    for entry in os.listdir(directory_path):
        items.append(entry)
    return items
