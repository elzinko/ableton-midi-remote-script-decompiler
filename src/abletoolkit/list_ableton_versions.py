import os
import glob
import platform

def list_ableton_versions():
    """
    Lists the installed versions of Ableton Live on the system and their installation paths.
    Works on macOS. For Windows, a different path would need to be used.
    """
    if platform.system() == "Darwin":  # macOS
        ableton_dirs = glob.glob("/Applications/Ableton Live*")
    else:
        print("This script currently only works on macOS.")
        return

    if not ableton_dirs:
        print("No Ableton Live installations found.")
    else:
        print("Installed versions of Ableton Live:")
        for path in ableton_dirs:
            version = os.path.basename(path)
            print(f"- {version} : {path}")

if __name__ == "__main__":
    list_ableton_versions()
