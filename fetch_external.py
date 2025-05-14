# This script fetches external repositories for the Brainglobe project.
# It checks if the repositories already exist in the specified paths,
# and if not, it clones them from their respective GitHub URLs.
# If they do exist, it pulls the latest changes from the remote repository.

import os
import subprocess

REPOS = [
    ("https://github.com/thisisrick25/brainglobe-atlasapi.git", "external/brainglobe-atlasapi", "test"),
    # ("https://github.com/brainglobe/brainglobe-space.git", "external/brainglobe-space"),
    # ("https://github.com/brainglobe/brainglobe-utils.git", "external/brainglobe-utils"),
    # ("https://github.com/brainglobe/brainreg.git", "external/brainreg"),
    # ("https://github.com/brainglobe/cellfinder.git", "external/cellfinder"),
    # Add more (url, path) pairs as needed
]

for url, path, branch in REPOS:
    if not os.path.exists(path):
        subprocess.run(["git", "clone", "--branch", branch, url, path])
    else:
        subprocess.run(["git", "-C", path, "fetch"], check=True)
        subprocess.run(["git", "-C", path, "checkout", branch], check=True)
        subprocess.run(["git", "-C", path, "pull", "origin", branch], check=True)
        
    subprocess.run(["pip", "install", "-e", path])