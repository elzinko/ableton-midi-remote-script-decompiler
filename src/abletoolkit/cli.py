"""
This module contains the command-line interface for the Abletoolkit package.
"""

import argparse
from abletoolkit import version
from abletoolkit.ableton.installation import get_ableton_installed_versions
from abletoolkit.ableton.scripts import get_midi_remote_script_directories
from abletoolkit.pyc.decompile import decompile
from abletoolkit.pyc.version import get_python_version

ATK_VERSION = version.__version__


def handle_ableton(args):
    """
    Handle the Ableton Live related commands.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.list:
        get_ableton_installed_versions()


def handle_scripts(args):
    """
    Handle the MIDI Remote Scripts related commands.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.list:
        get_midi_remote_script_directories()


def handle_pyc(args):
    """
    Handle the PYC file related commands.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.version:
        handle_pyc_version(args)
    elif args.decompile:
        handle_pyc_decompile(args)
    else:
        print("Please specify either --version or --decompile.")


def handle_pyc_decompile(args):
    """
    Handle the decompilation of a folder of .pyc files.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.src_dir and args.dest_dir:
        decompile(args.src_dir, args.dest_dir)
    else:
        print(
            "Please provide the path to the .pyc files"
            + " and the destination folder where it should be decompiled."
        )


def handle_pyc_version(args):
    """
    Handle the determination of the Python version used to compile a .pyc file.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.file_path:
        pyc_version = get_python_version(args.file_path)
        if pyc_version:
            print(f"The .pyc file was compiled with Python {pyc_version}")
        else:
            print("Failed to determine the Python version")
    else:
        print("Please provide the path to the .pyc file.")


def main():
    """
    Main entry point for the Abletoolkit command-line interface.
    """
    parser = argparse.ArgumentParser(
        description="Ableton Toolkit (ATK): A set of tools for working with Ableton Live.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("-v", "--version", action="version", version=f"{ATK_VERSION}")

    subparsers = parser.add_subparsers(dest="category")

    # atk ableton
    ableton_parser = subparsers.add_parser("ableton", help="Ableton-related tasks")
    ableton_subparsers = ableton_parser.add_subparsers(help="Ableton commands")

    # atk ableton --list
    ableton_list_parser = ableton_subparsers.add_parser(
        "list", help="List Ableton versions"
    )
    ableton_list_parser.set_defaults(func=get_ableton_installed_versions)

    # atk ableton --scripts
    ableton_scripts_parser = ableton_subparsers.add_parser(
        "scripts", help="List Ableton MIDI Remote Script directories"
    )
    ableton_scripts_parser.set_defaults(func=get_midi_remote_script_directories)

    # atk pyc
    pyc_parser = subparsers.add_parser("pyc", help="PYC-related tasks")
    pyc_subparsers = pyc_parser.add_subparsers(help="PYC commands")

    # atk pyc decompile
    decompile_parser = pyc_subparsers.add_parser(
        "decompile", help="Decompile a .pyc file"
    )
    decompile_parser.add_argument(
        "src_dir", help="Source folder for .pyc files to decompile"
    )
    decompile_parser.add_argument(
        "dest_dir", help="Destination folder for decompiles .py files"
    )
    decompile_parser.set_defaults(func=handle_pyc_decompile)

    # atk pyc version
    version_parser = pyc_subparsers.add_parser(
        "version", help="Get Python version from .pyc file"
    )
    version_parser.add_argument("pyc_file", help="Input .pyc file path")
    version_parser.set_defaults(func=handle_pyc_version)

    args = parser.parse_args()
    if args.category:
        if args.func.__code__.co_argcount == 0:
            args.func()
        else:
            args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
