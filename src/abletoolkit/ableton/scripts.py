"""
This submodule contains functions to determine the Python version used to compile a .pyc file.
"""

import glob
import platform
from pathlib import Path


def get_midi_remote_script_directories():
    """
    Lists the Ableton directories where midi remote scripts are deployed.
    """
    if platform.system() == "Darwin":  # macOS
        user_dir = Path.home()
        remote_scripts_dirs = [
            "/Applications/Ableton Live*/Contents/App-Resources/MIDI Remote Scripts",
            f"{user_dir}/Music/Ableton/User Library/Remote Scripts",
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
        for found_dir in found_dirs:
            print(f"- {found_dir}")
