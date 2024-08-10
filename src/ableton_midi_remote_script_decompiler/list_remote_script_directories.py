import glob
import platform
from pathlib import Path

def list_remote_script_directories():
    """
    Liste les répertoires où les MIDI Remote Scripts sont déployés.
    Inclut un chemin spécifique pour macOS.
    """
    if platform.system() == "Darwin":  # macOS
        user_dir = Path.home()
        remote_scripts_dirs = [
            "/Applications/Ableton Live*/Contents/App-Resources/MIDI Remote Scripts",
            f"{user_dir}/Music/Ableton/User Library/Remote Scripts"
        ]
    else:
        print("Ce script fonctionne uniquement sous macOS pour le moment.")
        return

    found_dirs = []
    for directory in remote_scripts_dirs:
        expanded_dirs = glob.glob(directory)
        found_dirs.extend(expanded_dirs)

    if not found_dirs:
        print("Aucun répertoire de MIDI Remote Scripts trouvé.")
    else:
        print("Répertoires de MIDI Remote Scripts trouvés :")
        for dir in found_dirs:
            print(f"- {dir}")

if __name__ == "__main__":
    list_remote_script_directories()
