"""
Test the decompile module.
The tests are based on tests/decompile/ableton/11/midi_remote_scripts and tests/decompile/ableton/12/midi_remote_scripts.
Decompiled files will be copied into tests/decompile/decompiled/ableton/11/midi_remote_scripts tests/decompile/decompiled/ableton/12/midi_remote_scripts and check if the decompiled files exist.
A variable is used to know how many ableton version are provided in tests/decompile/ableton folder.
"""

import os
import unittest
import shutil
from pathlib import Path
from abletoolkit.decompile import decompile_ableton_scripts


class TestDecompile(unittest.TestCase):
    """
    This class contains unit tests for the decompile functionality.

    Args:
        unittest (type): The base class for all test cases.
    """

    def setUp(self):
        self.ableton_path = Path(__file__).parent / "decompile" / "ableton"
        self.decompiled_path = (
            Path(__file__).parent / "decompile" / "decompiled" / "ableton"
        )
        self.ableton_version_folders = [
            folder
            for folder in os.listdir(self.ableton_path)
            if os.path.isdir(self.ableton_path / folder)
        ]
        print(f"Found Ableton versions: {self.ableton_version_folders}")

    def tearDown(self):
        for version in self.ableton_version_folders:
            output_dir = self.decompiled_path / version / "midi_remote_scripts"
            print(f"Removing {output_dir}")
            shutil.rmtree(output_dir)

    def test_decompile_ableton_scripts(self):
        """
        Test the decompile_ableton_scripts function.
        """
        for version in self.ableton_version_folders:
            source_dir = self.ableton_path / version / "midi_remote_scripts"
            output_dir = self.decompiled_path / version / "midi_remote_scripts"
            print(f"Decompiling {source_dir} to {output_dir}")
            decompile_ableton_scripts(source_dir, output_dir)
            for root, dirs, files in os.walk(output_dir):
                for file in files:
                    self.assertTrue(os.path.exists(os.path.join(root, file)))


if __name__ == "__main__":
    unittest.main()
