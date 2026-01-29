from scanner import scan_directory
from organizer import decide_targets
from mover import move_files

BASE_DIR = "test_data"

if __name__ == "__main__":
    scanned = scan_directory(BASE_DIR)
    targets = decide_targets(scanned)
    move_files(targets, BASE_DIR)