EXTENSION_MAP = {
    "documents": [".pdf", ".docx", ".txt"],
    "images": [".png", ".jpg", ".jpeg"],
    "audio": [".mp3", ".wav"]
}

def decide_targets(scanned_items):
    targets = {}

    for item in scanned_items:
        if item["type"] == "directory":
            print(f"skipping directory: {item['path']}")
            continue

        extension = item["extension"]
        target_folder = None

        if extension:
            for category, extensions in EXTENSION_MAP.items():
                if extension in extensions:
                    target_folder = category
                    break
        
        if target_folder:
            targets[item["path"]] = target_folder
        else:
            targets[item["path"]] = "others"

    return targets

if __name__ == "__main__":
    sample = [
        {"path": "a.pdf", "type": "file", "extension": ".pdf"},
        {"path": "b.png", "type": "file", "extension": ".png"},
        {"path": "c", "type": "file", "extension": None},
        {"path": "folder", "type": "directory", "extension": None}
    ]

    print(decide_targets(sample))

"""
output:
(PSL) C:\Users\milind dhawle\OneDrive\Desktop\python-practice-labs>python file_organizer\organizer.py
skipping directory: folder
{'a.pdf': 'documents', 'b.png': 'images', 'c': 'others'}

"""