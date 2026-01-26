def decide_targets(scanned_items):
    """
    Decide target folders for files based on metadata.

    Args:
        scanned_items (list): Output from scanner.scan_directory

    Returns:
        dict: mapping of file path to target folder name
    """
    targets = {}
    return targets