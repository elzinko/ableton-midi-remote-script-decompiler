import argparse
from abletoolkit.decompile import decompile_ableton_scripts
from abletoolkit.list_ableton_versions import list_ableton_versions
from abletoolkit.list_remote_script_directories import list_remote_script_directories

def main():
    parser = argparse.ArgumentParser(description="Outils de décompilation pour Ableton Live.")
    subparsers = parser.add_subparsers(dest="command")

    # Sous-commande pour décompiler
    decompile_parser = subparsers.add_parser('decompile', help='Décompiler les fichiers compilés d\'Ableton.')
    decompile_parser.add_argument('source', type=str, help='Chemin du répertoire source contenant les fichiers compilés.')
    decompile_parser.add_argument('output', type=str, help='Chemin du répertoire où stocker les fichiers décompilés.')

    # Sous-commande pour lister les versions d'Ableton installées
    subparsers.add_parser('list_versions', help='Lister les versions d\'Ableton installées.')

    # Sous-commande pour lister les répertoires des Remote Scripts
    subparsers.add_parser('list_remote_scripts', help='Lister les répertoires des MIDI Remote Scripts.')

    args = parser.parse_args()

    if args.command == "decompile":
        decompile_ableton_scripts(args.source, args.output)
    elif args.command == "list_versions":
        list_ableton_versions()
    elif args.command == "list_remote_scripts":
        list_remote_script_directories()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
