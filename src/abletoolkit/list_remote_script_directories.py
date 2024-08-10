import glob
import platform
from pathlib import Path

def list_remote_script_directories():
    """
    Lists the directories where MIDI Remote Scripts are deployed.
    Includes a specific path for macOS.
    """
    if platform.system() == "Darwin":  # macOS
        user_dir = Path.home()
        remote_scripts_dirs = [
            "/Applications/Ableton Live*/Contents/App-Resources/MIDI Remote Scripts",
            f"{user_dir}/Music/Ableton/User Library/Remote Scripts"
        ]
    else:
        print("This script currently only works on macOS.")
        return

    found_dirs = []
    for directory in remote_scripts_dirs:
        expanded_dirs = glob.glob(directory)
        found_dirs.extend(expanded_dirs)

    if not found_dirs:
        print("No MIDI Remote Scripts directories found.")
    else:
        print("Found MIDI Remote Scripts directories:")
        for dir in found_dirs:
            print(f"- {dir}")

if __name__ == "__main__":
    list_remote_script_directories()
