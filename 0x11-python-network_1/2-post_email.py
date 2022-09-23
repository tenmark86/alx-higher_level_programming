#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    reqq = urllib.request.Request(sys.argv[1], data)

    try:
        with urllib.request.urlopen(reqq) as resp:
            if resp is not None:
                html = resp.read()
                print(html.decode('utf-8'))
    except Exception:
        pass
