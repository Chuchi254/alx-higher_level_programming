#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using requests.
"""


import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- typee:", type(body))
    print("\t- content:", body)
