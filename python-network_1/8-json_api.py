#!/usr/bin/python3
""" Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""


import requests
import sys


if __name__ == '__main__':
    data = {"q": ""}

    try:
        data['q'] = [sys.argv[1]]
    except:
        pass
    req = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_1 = req.json()
        if not json_1:
            print("No result")
        else:
            print("{} {}".format(json_1.get('[id]'), json_1.get('name')))
    except:
        print("Not a valid JSON")
