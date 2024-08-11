"""
Description:
    Determines the Python version used to compile a .pyc file using xdis.
Args:
    pyc_file_path (str): The path to the .pyc file.
Returns:
    str: The Python version as a string (e.g., '3.7', '3.8').
    None: If the version cannot be determined.
"""

import sys
from xdis import load_module


def get_python_version_from_pyc(pyc_file_path):
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


# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: get_python_version_from_pyc <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    version = get_python_version_from_pyc(file_path)
    if version:
        print(f"The .pyc file was compiled with Python {version}")
    else:
        print("Failed to determine the Python version")
