"""
This file is used to package the project.
"""

from setuptools import setup, find_packages

# from setuptools.command.egg_info import egg_info as _egg_info
from src.abletoolkit import version as version_module

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()


# class EggInfo(_egg_info):
#     """
#     This class is used to change the default egg_info folder to the build folder.

#     Args:
#         _egg_info (class): The default egg_info class.
#     """

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.egg_base = "build"

#     def initialize_options(self):
#         _egg_info.initialize_options(self)


setup(
    name="abletoolkit",
    version=version_module.__version__,
    description="Ableton Live developper toolkit.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Thomas Couderc",
    author_email="thomas.couderc@gmail.com",
    url="https://github.com/elzinko/abletoolkit",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # cmdclass={"egg_info": EggInfo},
    command_options={
        "egg_info": {
            "egg_base": ("setup.py", "build/"),
        }
    },
    entry_points={
        "console_scripts": [
            "abletoolkit=abletoolkit.cli:main",
            "atk=abletoolkit.cli:main",
        ],
    },
    install_requires=[
        "uncompyle6",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL 3 License",
        "Operating System :: OSX",
    ],
    python_requires=">=3.12.1",
)
