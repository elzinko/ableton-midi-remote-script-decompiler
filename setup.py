"""
This file is used to package the project.
It is used by the `pip` command to install the project.
To install the project, run the following command:
```
pip install .
```
"""

from setuptools import setup, find_packages
from src.abletoolkit import version as version_module

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="abletoolkit",
    version=version_module.__version__,
    description="Ableton Live user toolkit.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Thomas Couderc",
    author_email="thomas.couderc@gmail.com",
    url="https://github.com/elzinko/abletoolkit",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
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
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.1",
)
