#!/usr/bin/python3
"""
Python script that
fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status "
    with request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("-\t type:", type(html))
        print("-\t content:", html)
        print("-\t utf8 content:", html.decode("utf-8"))
