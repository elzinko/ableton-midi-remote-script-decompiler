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


def main():
    """
    Main entry point for the Abletoolkit command-line interface.
    """

    parser = argparse.ArgumentParser(
        description="Ableton Toolkit (ATK): A set of tools for working with Ableton Live."
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{ATK_VERSION}"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Ableton versions listing sub-command
    subparsers.add_parser(
        "ableton_versions",
        help="List installed versions of Ableton Live.",
        aliases=["av"],
    )

    # MIDI remote scripts listing sub-command
    subparsers.add_parser(
        "list_remote_scripts",
        help="List directories of MIDI Remote Scripts.",
        aliases=["lrs"],
    )

    # PYC version sub-command
    pyc_version_parser = subparsers.add_parser(
        "pyc_version",
        help="Determine the Python version used to compile a .pyc file.",
        aliases=["pycv"],
    )
    pyc_version_parser.add_argument(
        "file_path",
        type=str,
        help="Path to the .pyc file.",
    )

    # Sub-command for decompiling
    decompile_parser = subparsers.add_parser(
        "decompile",
        help="Decompile Ableton compiled files.",
        aliases=["d"],
    )
    decompile_parser.add_argument(
        "source",
        type=str,
        help="Path to the source directory containing compiled files.",
    )
    decompile_parser.add_argument(
        "output",
        type=str,
        help="Path to the output directory to store decompiled files.",
    )

    args = parser.parse_args()

    if args.command in ["list_versions", "lv"]:
        list_ableton_versions()
    elif args.command in ["list_remote_scripts", "lrs"]:
        list_remote_script_directories()
    elif args.command in ["pyc_version", "pyc"]:
        if args.version:
            pyc_version = get_python_version_from_pyc(args.file_path)
            if pyc_version:
                print(f"The .pyc file was compiled with Python {pyc_version}")
            else:
                print("Failed to determine the Python version")
        else:
            parser.print_help()
    elif args.command in ["decompile", "dcp"]:
        decompile(args.source, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
