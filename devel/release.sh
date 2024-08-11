#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")/.."

# Ensure the script is run with a version argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <version>"
    exit 1
fi

NEW_VERSION=$1

# Step 1: Update the version in version.py
echo """
Version of the package.
""" > src/abletoolkit/version.py
echo "__version__ = \"$NEW_VERSION\"" >> src/abletoolkit/version.py

# Step 2: Update CHANGELOG.md (Manual step recommended)
echo "Please update CHANGELOG.md manually and press enter to continue..."
read

# Step 3: Commit changes and tag the release
git add src/abletoolkit/version.py CHANGELOG.md
git commit -m "Bump version to $NEW_VERSION and update changelog."
git tag -a "v$NEW_VERSION" -m "Release version $NEW_VERSION"
git push origin "v$NEW_VERSION"

# Step 4: Build the package
python setup.py sdist bdist_wheel

# Step 5: Publish the package to PyPI
twine upload dist/*

# Step 6: Clean up
rm -rf build dist *.egg-info
