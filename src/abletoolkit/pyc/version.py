"""
This submodule contains functions to determine the Python version used to compile a .pyc file.
"""

import os
from xdis import load_module

SUBPROCESS = "subprocess"
EMBEDED = "embeded"
METHOD = SUBPROCESS


def print_python_version(pyc_file_path):
    """
    Get the Python version used to compile a .pyc file and print it to the console.

    Args:
        pyc_file_path (str): The path to the .pyc file.
    """
    if not os.path.exists(pyc_file_path):
        print(f"The file {pyc_file_path} does not exist.")
        return

    version = get_python_version(pyc_file_path)
    if version:
        print(f"The .pyc file was compiled with Python {version}")
    else:
        print("Failed to determine the Python version")


def get_python_version(pyc_file_path):
    """
    Determines the Python version used to compile a .pyc file using xdis.

    Args:
        pyc_file_path (str): The path to the .pyc file.

    Returns:
        str: The Python version as a string (e.g., '3.7', '3.8').
        None: If the version cannot be determined.
    """
    try:
        py_version, _, _, _, _, _, _ = load_module(pyc_file_path)
        print(f"py_version: {py_version}")
        return f"{py_version[0]}.{py_version[1]}"
    except (ModuleNotFoundError, ImportError) as e:
        print(f"Error determining Python version: {e}")
        return None
