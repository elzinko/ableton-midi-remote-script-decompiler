from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="abletoolkit",
    version="0.1.0",
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
        ],
    },
    install_requires=[
        "uncompyle6",
        # Ajouter d'autres dépendances si nécessaire
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.1",
)
