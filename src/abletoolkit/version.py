"""
Version package.
"""

import subprocess

def get_last_tag():
    """
    Get last git tag that describe a version
    Returns:
        string: last git tag at format 'X.Y.Z'
    """
    try:
        git_tag = subprocess.check_output(
            ['git', 'describe', '--tags', '--abbrev=0']
        ).strip().decode('utf-8')
        return git_tag
    except subprocess.CalledProcessError:
        return None

__version__ = get_last_tag()
