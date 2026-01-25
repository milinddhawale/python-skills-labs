import os

def scan_directory(directory_path):
    items = []

    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        
        if os.path.isdir(full_path):
            item_type = "directory"
            extension = None
        else:
            item_type = "file"
            ext = os.path.splitext(entry)[1].lower()
            extension = ext if ext else None

        item_info = {
            "name": entry,
            "path": full_path,
            "type": item_type,
            "extension": extension
        }

        items.append(item_info)

    return items

if __name__ == "__main__":
    result = scan_directory(".")
    for item in result:
        print(item)

