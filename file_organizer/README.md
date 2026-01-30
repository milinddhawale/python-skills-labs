# File Organizer

A simple, modular Python tool that organizes files in a directory
into categorized folders based on file extensions.

## Problem
Directories like Downloads often become cluttered with mixed files.
Manually sorting them is repetitive and error-prone.

## Solution
This tool follows a clean, three-step pipeline:

1. **Scan** the directory and collect file metadata
2. **Decide** the target folder for each file
3. **Move** files into organized folders

## Project Structure
file_organizer/
├── scanner.py # Reads directory and returns metadata
├── organizer.py # Decides target folders for files
├── mover.py # Moves files on the filesystem
├── main.py # Entry point that wires everything together


## How It Works
- Files are grouped by extension:
  - `.pdf`, `.docx`, `.txt` → documents
  - `.png`, `.jpg`, `.jpeg` → images
  - `.mp3`, `.wav` → audio
  - no / unknown extension → others
- Directories are ignored safely

## Usage

```bash
python main.py

## Exppected Output
test_data/
├── documents/
│   ├── resume.pdf
│   ├── notes.txt
├── images/
│   └── image.png
├── audio/
│   └── song.mp3
├── others/
│   └── README
├── subfolder/   (untouched)
