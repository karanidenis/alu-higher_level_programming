#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
 using the package requests"""

import urllib.request
if __name__ == '__main__':
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as file:
        print("Body response:")
        print('\t- type: {}'.format(type(file)))
        print('\t- content: {}'.format(file))
