#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    try:
        req.raise_for_status()
        print(req.text)

    except Exception as e:
        print("Error code:", req.status_code)
