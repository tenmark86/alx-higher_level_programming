#!/usr/bin/python3
"""
GET request and printing error code if it exist
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            if resp is not None:
                html = resp.read()
                print(html.decode('utf-8'))
    except urllib.error.HTTPError as fail:
        print('Error code: {}'.format(fail.code))
