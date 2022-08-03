#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.

"""

import requests
import sys


if __name__ == '__main__':
    try:
        repository = sys.argv[1]
        owner_name = sys.argv[2]
        url = 'https://developer.github.com/v3/repos/{}/{}/commits'.format(owner_name, repository)
        req = requests.get(url)
        json_o = req.json()
        for i in range(0, 10):
            print("{}: {}".format(json_o[i].get('sha'), json_o[i].get('commit')
                                  .get('author').get('name')))
    except:
        pass


