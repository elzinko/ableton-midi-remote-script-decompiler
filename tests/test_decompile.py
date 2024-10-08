"""
Test the decompile module.

The tests are based on files in :
- tests/decompile/ableton/11/midi_remote_scripts
- tests/decompile/ableton/12/midi_remote_scripts.

Decompiled files will be copied into :
- tests/decompile/decompiled/ableton/11/midi_remote_scripts
- tests/decompile/decompiled/ableton/12/midi_remote_scripts
"""

import os
import unittest
import shutil
from pathlib import Path

from src.abletoolkit.pyc.decompile import decompile


class TestDecompile(unittest.TestCase):
    """
    This class contains unit tests for the decompile functionality.

    Args:
        unittest (type): The base class for all test cases.
    """

    def setUp(self):
        self.build_path = Path(__file__).parent.parent / "build"
        self.ableton_path = (
            Path(__file__).parent / "resources" / "decompile" / "ableton"
        )
        self.decompiled_path = self.build_path / "decompile" / "ableton"
        self.ableton_version_folders = [
            folder
            for folder in os.listdir(self.ableton_path)
            if os.path.isdir(self.ableton_path / folder)
        ]
        print(f"Found Ableton versions: {self.ableton_version_folders}")

    def tearDown(self) -> None:
        # remove the decompiled files
        shutil.rmtree(self.decompiled_path.parent)

    def test_decompile_ableton_scripts(self):
        """
        Test the decompile_ableton_scripts function.
        """
        for version in self.ableton_version_folders:
            input_dir = self.ableton_path / version / "midi_remote_scripts"
            output_dir = self.decompiled_path / version / "midi_remote_scripts"
            print(f"Decompiling {input_dir} to {output_dir}")
            decompile(input_dir, output_dir)
            for root, _, files in os.walk(output_dir):
                for file in files:
                    self.assertTrue(os.path.exists(os.path.join(root, file)))


if __name__ == "__main__":
    unittest.main()
