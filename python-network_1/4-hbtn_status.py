#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
 using the package requests"""

import requests


if __name__ == '__main__':
    req = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print('\t- type: {}'.format(type(req)))
    print('\t- content: {}'.format(req))
