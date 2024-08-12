"""
This module contains the tests for the pyc_version module.
"""

import unittest
from pathlib import Path
from src.abletoolkit.pyc.version import get_python_version


class TestPycVersion(unittest.TestCase):
    """
    Test the ability to determine the Python version used to compile a .pyc file.

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.pyc_file_ableton_11 = (
            Path(__file__).parent
            / "resources"
            / "decompile"
            / "ableton"
            / "11"
            / "midi_remote_scripts"
            / "Push"
            / "push.pyc"
        )
        self.pyc_file_ableton_12 = (
            Path(__file__).parent
            / "resources"
            / "decompile"
            / "ableton"
            / "12"
            / "midi_remote_scripts"
            / "Push"
            / "push.pyc"
        )

    def test_python_version(self):
        """
        Test if the .pyc file compiled with Python 3.7 is correctly identified.
        """
        version = get_python_version(self.pyc_file_ableton_11)
        self.assertEqual(version, "3.7", f"Expected '3.7', but got '{version}'")

    def test_python_version_38(self):
        """
        Test if the .pyc file compiled with Python 3.7 is correctly identified.
        """
        version = get_python_version(self.pyc_file_ableton_12)
        self.assertEqual(version, "3.7", f"Expected '3.7', but got '{version}'")


if __name__ == "__main__":
    unittest.main()
