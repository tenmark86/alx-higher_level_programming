#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of the variable
"""

import requests
import sys


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp is not None:
        print(resp.headers.get('X-Request-Id'))
