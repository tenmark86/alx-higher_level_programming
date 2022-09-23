#!/usr/bin/python3
"""
Write a Python script that takes your
GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests


if __name__ == "__main__":
    resp = requests.get("https://api.github.com/user", auth=(
            sys.argv[1], sys.argv[2]))
    result = resp.json()
    print(result.get("id"))
