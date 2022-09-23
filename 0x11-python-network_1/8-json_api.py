#!/usr/bin/python3
"""
Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = {"q": ""}
    else:
        letter = {"q": sys.argv[1]}
    resp = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        result = resp.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")
