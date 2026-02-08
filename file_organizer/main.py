import argparse

from scanner import scan_directory
from organizer import decide_targets
from mover import move_files

def parse_args():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by file type"
    )

    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Directory path to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show what would happen without moving files"
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    scanned = scan_directory(args.path)
    targets = decide_targets(scanned)
    move_files(targets, args.path)