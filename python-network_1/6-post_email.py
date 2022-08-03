#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import requests
import sys

if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    req = requests.get(sys.argv[1], values)
    with requests.urlopen(req) as qer:
        print(qer.read().decode('utf-8'))
