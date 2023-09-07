import ctypes
import os
from send2trash import send2trash

# Define the paths to the temporary folders
system_temp_folder = os.path.join(os.environ["SystemRoot"], "Temp")  # %systemdrive%\Windows\Temp
user_temp_folder = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Temp")  # %userprofile%\AppData\Local\Temp

def move_contents_to_recycle_bin(folder_path):
    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                send2trash(file_path)
                print(f"Moved to Recycle Bin: {file_path}")
    except Exception as e:
        print(f"Error moving files to Recycle Bin in {folder_path}: {e}")

def empty_recycle_bin():
    SHELL32 = ctypes.windll.shell32
    confirm = 1  # Set to 1 to skip the confirmation dialog (SHERB_NOCONFIRMATION)

    # SHEmptyRecycleBinW function
    result = SHELL32.SHEmptyRecycleBinW(None, None, confirm)
    
    if result == 0:
        print("Recycle Bin emptied successfully.")
    else:
        print("Failed to empty Recycle Bin.")

if __name__ == "__main__":
    move_contents_to_recycle_bin(system_temp_folder)
    move_contents_to_recycle_bin(user_temp_folder)
    empty_recycle_bin()
    print("Script executed successfully.")