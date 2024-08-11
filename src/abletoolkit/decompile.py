"""
This module provides a function to decompile all .pyc or .pyo files in a directory
"""

import os
import sys
from pathlib import Path
import uncompyle6


def decompile(source_dir, output_dir):
    """
    Decompiles all .pyc files in the source directory
    and places them in the output directory.
    """
    if not os.path.exists(source_dir):
        msg = f"The source directory {source_dir} does not exist."
        raise FileNotFoundError(msg)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith((".pyc")):
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_dir)
                output_file_dir = os.path.join(output_dir, relative_path)

                Path(output_file_dir).mkdir(parents=True, exist_ok=True)

                output_file_path = os.path.join(output_file_dir, file[:-1] + "py")

                try:
                    with open(output_file_path, "w", encoding="utf-8") as output_file:
                        uncompyle6.decompile_file(
                            source_file_path, outstream=output_file
                        )
                    print(f"Decompiled: {source_file_path} -> {output_file_path
                    }")
                except (FileNotFoundError, IOError) as e:
                    print(f"Error during decompilation of {source_file_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decompile.py <source_directory> <output_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    output_directory = sys.argv[2]

    decompile(source_directory, output_directory)
