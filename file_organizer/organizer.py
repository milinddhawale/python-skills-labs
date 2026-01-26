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

    return targets
