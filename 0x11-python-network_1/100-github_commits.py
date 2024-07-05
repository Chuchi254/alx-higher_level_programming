#!/usr/bin/python3
"""
This script list the 10 most recent commits of a given repository by a given
owner using the GitHub API.
"""


import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    
    response = requests.get(url)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
        except (TypeError, KeyError, IndexError):
            pass
