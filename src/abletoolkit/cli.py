"""
This module contains the command-line interface for the Abletoolkit package.
"""

import argparse
from src.abletoolkit.decompile import decompile_ableton_scripts
from src.abletoolkit.list_ableton_versions import list_ableton_versions
from src.abletoolkit.list_remote_script_directories import (
    list_remote_script_directories,
)

from src.abletoolkit.pyc_version import get_python_version_from_pyc


def main():
    """
    Main entry point for the Abletoolkit command-line interface.
    """

    parser = argparse.ArgumentParser(
        description="Outils de décompilation pour Ableton Live."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Sous-commande pour décompiler
    decompile_parser = subparsers.add_parser(
        "decompile", help="Décompiler les fichiers compilés d'Ableton."
    )
    decompile_parser.add_argument(
        "source",
        type=str,
        help="Chemin du répertoire source contenant les fichiers compilés.",
    )
    decompile_parser.add_argument(
        "output",
        type=str,
        help="Chemin du répertoire où stocker les fichiers décompilés.",
    )

    # Ableton versions listing sub command
    subparsers.add_parser(
        "list_versions", help="Lister les versions d'Ableton installées."
    )

    # midi remote scripts listing sub command
    subparsers.add_parser(
        "list_remote_scripts", help="Lister les répertoires des MIDI Remote Scripts."
    )

    # pyc version sub command
    pyc_version_parser = subparsers.add_parser(
        "pyc_version",
        help="Déterminer la version de Python utilisée pour compiler un fichier .pyc.",
    )

    pyc_version_parser.add_argument(
        "file_path",
        type=str,
        help="Chemin du fichier .pyc.",
    )

    args = parser.parse_args()

    if args.command == "decompile":
        decompile_ableton_scripts(args.source, args.output)
    elif args.command == "list_versions":
        list_ableton_versions()
    elif args.command == "list_remote_scripts":
        list_remote_script_directories()
    elif args.command == "pyc_version":
        version = get_python_version_from_pyc(args.file_path)
        if version:
            print(f"The .pyc file was compiled with Python {version}")
        else:
            print("Failed to determine the Python version")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
