#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the response header.
"""
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1]).text
    print(req.info()['X-Request-Id'])
