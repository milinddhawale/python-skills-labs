def decide_targets(scanned_items):
    targets = {}

    for item in scanned_items:
        if item["type"] == "directory":
            print(f"skipping directory: {item['path']}")
            continue

    return targets