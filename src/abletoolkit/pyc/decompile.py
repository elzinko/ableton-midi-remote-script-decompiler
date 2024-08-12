"""
This submodule contains functions to determine the Python version used to compile a .pyc file.
"""

import os
import subprocess
import sys
from pathlib import Path
import uncompyle6

SUBPROCESS = "subprocess"
EMBEDED = "embeded"
METHOD = SUBPROCESS


def decompile(src_dir, dest_dir):
    """
    Decompiles all .pyc files from the source directory

    :param src_dir: Folder containing the .pyc files to decompile.
    :param dest_dir: Folder to output the decompiled .py files.
    """
    if METHOD == SUBPROCESS:
        decompile_subprocess(src_dir, dest_dir)
    elif METHOD == EMBEDED:
        decompile_embeded(src_dir, dest_dir)
    else:
        print("Unkown method", file=sys.stderr)
        sys.exit(1)


def decompile_embeded(src_dir, dest_dir):
    """
    Decompiles all .pyc files from the source directory
    and places them in the destination directory.
    """
    if not os.path.exists(src_dir):
        msg = f"The source directory {src_dir} does not exist."
        raise FileNotFoundError(msg)

    if dest_dir is None:
        decompile_folder(src_dir)
    elif not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith((".pyc")):
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, src_dir)
                output_file_dir = os.path.join(dest_dir, relative_path)

                Path(output_file_dir).mkdir(parents=True, exist_ok=True)

                output_file_name = file[:-1]  # from .pyc to .py
                output_file_path = os.path.join(output_file_dir, output_file_name)
                output_file_path = os.path.normpath(output_file_path)

                try:
                    with open(output_file_path, "w", encoding="utf-8") as output_file:
                        uncompyle6.decompile_file(
                            source_file_path, outstream=output_file
                        )
                    print(f"Decompiled: {source_file_path} -> {output_file_path}")
                    continue
                except (FileNotFoundError, IOError) as e:
                    print(f"Error during decompilation of {source_file_path}: {e}")
                    continue


def decompile_subprocess(src_dir, dest_dir):
    """
    Decompiles all .pyc files from the source directory.
    Places them in the destination directory.

    :param src_dir: Folder containing the .pyc files to decompile.
    :param dest_dir: Folder to output the decompiled .py files.
    """
    try:
        command = f"uncompyle6 -r -o {dest_dir} {src_dir}"

        print(f"Running command: {command}")

        # check if source directory exists
        if not os.path.exists(src_dir):
            print(f"Source folder {src_dir} does not exist.", file=sys.stderr)
            sys.exit(1)

        # if dest_dir does not exists, then create it
        if not os.path.exists(dest_dir):
            print(f"Destination folder {dest_dir} does not exist. Creating it.")
            os.makedirs(dest_dir)

        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        print(result.stdout.decode())
        if result.stderr:
            print("Error:", result.stderr.decode(), file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error during decompilation: {e}", file=sys.stderr)


def decompile_folder(src_dir):
    """
    Decompiles all .pyc files in the source directory.
    If source_dir contains subdirectories, the decompiled files will be
    placed in the same subdirectory structure in the output directory.
    Subdirectories and files are handled alphabetically.
    Logs are printed to the console so that we can see which files have
    been decompiled and where errors have occurred.

    Args:
        src_dir (str): The directory containing the .pyc files to decompile
    """
    if not os.path.exists(src_dir):
        msg = f"The source directory {src_dir} does not exist."
        raise FileNotFoundError(msg)

    for root, dirs, files in os.walk(src_dir, topdown=True):
        dirs.sort()
        files.sort()
        for file in files:
            if file.endswith((".pyc", ".pyo")):
                source_file_path = os.path.join(root, file)
                output_file_dir = os.path.join(root, "decompiled")
                Path(output_file_dir).mkdir(parents=True, exist_ok=True)

                output_file_name = file[:-1] + "y"
                output_file_path = os.path.join(output_file_dir, output_file_name)
                output_file_path = os.path.normpath(output_file_path)

                try:
                    with open(output_file_path, "w", encoding="utf-8") as output_file:
                        try:
                            uncompyle6.decompile_file(
                                source_file_path, outstream=output_file
                            )
                        except (FileNotFoundError, IOError) as e:
                            print(
                                f"Error during decompilation of {source_file_path}: {e}"
                            )
                            continue
                    print(f"Decompiled: {source_file_path} -> {output_file_path}")
                except (FileNotFoundError, IOError) as e:
                    print(f"Error during decompilation of {source_file_path}: {e}")
                    continue
