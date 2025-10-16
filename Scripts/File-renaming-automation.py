import os
import re
import shutil
from datetime import datetime
from tkinter import Tk, filedialog

def get_directory():
    """Open a dialog to select a directory and return its path."""
    root = Tk()
    root.withdraw()  # Hide the root window
    directory = filedialog.askdirectory(title="Select Directory")
    return directory

def rename_files_in_directory(directory):
    """Rename all files in a directory based on their creation date."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            new_filename = f"{creation_date}_{filename}"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")
        else:
            print(f"Skipped {filename}, not a file.")

if __name__ == "__main__":
    selected_directory = get_directory()
    if selected_directory:
        rename_files_in_directory(selected_directory)
    else:
        print("No directory selected.")


