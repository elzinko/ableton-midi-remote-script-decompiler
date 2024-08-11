"""
This module contains the command-line interface for the Abletoolkit package.
"""

import argparse
from abletoolkit import version
from abletoolkit.decompile import decompile
from abletoolkit.pyc_version import get_python_version_from_pyc
from abletoolkit.list_ableton_versions import list_ableton_versions
from abletoolkit.list_remote_script_directories import list_remote_script_directories

ATK_VERSION = version.__version__

def handle_ableton(args):
    """
    Handle the Ableton Live related commands.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.list:
        list_ableton_versions()

def handle_scripts(args):
    """
    Handle the MIDI Remote Scripts related commands.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.list:
        list_remote_script_directories()

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

def handle_pyc_version(args):
    """
    Handle the determination of the Python version used to compile a .pyc file.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.file_path:
        pyc_version = get_python_version_from_pyc(args.file_path)
        if pyc_version:
            print(f"The .pyc file was compiled with Python {pyc_version}")
        else:
            print("Failed to determine the Python version")
    else:
        print("Please provide the path to the .pyc file.")

def handle_pyc_decompile(args):
    """
    Handle the decompilation of a .pyc file.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.
    """
    if args.file_path and args.output_dir:
        decompile(args.file_path, args.output_dir)
    else:
        print("Please provide the path to the .pyc file and the output directory.")

command_handlers = {
    "ableton": handle_ableton,
    "scripts": handle_scripts,
    "pyc": handle_pyc
}

def main():
    """
    Main entry point for the Abletoolkit command-line interface.
    """
    parser = argparse.ArgumentParser(
        description="Ableton Toolkit (ATK): A set of tools for working with Ableton Live.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-v", "--version", action="version", version=f"ATK {ATK_VERSION}")

    subparsers = parser.add_subparsers(dest="category")

    # Sub-command for Ableton-related actions
    ableton_parser = subparsers.add_parser(
        "ableton",
        help="Ableton Live related commands"
    )
    ableton_parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List installed versions of Ableton Live."
    )

    # Sub-command for MIDI Remote Scripts actions
    scripts_parser = subparsers.add_parser(
        "scripts",
        help="MIDI Remote Scripts related commands"
    )
    scripts_parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List directories of MIDI Remote Scripts."
    )

    # Sub-command for PYC file actions
    pyc_parser = subparsers.add_parser(
        "pyc", help="PYC file related commands"
    )
    pyc_parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Determine the Python version used to compile a .pyc file."
    )
    pyc_parser.add_argument(
        "-d", "--decompile",
        action="store_true",
        help="Decompile a .pyc file."
    )
    pyc_parser.add_argument(
        "file_path",
        nargs="?",
        type=str,
        help="Path to the .pyc file."
    )
    pyc_parser.add_argument(
        "output_dir",
        nargs="?",
        type=str,
        help="Output directory for decompiled files."
    )

    args = parser.parse_args()
    if args.category in command_handlers:
        command_handlers[args.category](args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
