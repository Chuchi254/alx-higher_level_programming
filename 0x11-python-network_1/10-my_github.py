#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and personal access
token) and uses the GitHub API to display your user ID.
"""


import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        json_response = response.json()
        print(json_response.get('id'))
    except ValueError:
        print("None")
