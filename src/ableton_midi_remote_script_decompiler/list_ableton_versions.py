import os
import glob
import platform

def list_ableton_versions():
    """
    Liste les versions d'Ableton Live installées sur le système et leurs chemins d'installation.
    Fonctionne sous macOS. Pour Windows, un chemin différent doit être utilisé.
    """
    if platform.system() == "Darwin":  # macOS
        ableton_dirs = glob.glob("/Applications/Ableton Live*")
    else:
        print("Ce script fonctionne uniquement sous macOS pour le moment.")
        return

    if not ableton_dirs:
        print("Aucune installation d'Ableton Live trouvée.")
    else:
        print("Versions d'Ableton Live installées :")
        for path in ableton_dirs:
            version = os.path.basename(path)
            print(f"- {version} : {path}")

if __name__ == "__main__":
    list_ableton_versions()
