#!/usr/bin/python3
""" A script that takes github credentials and uses the GitHubAPI
    to display id
"""
import sys
import requests


if __name__ == "__main__":
    uname = sys.argv[1]
    psswd = sys.argv[2]

    url = f'https://api.github.com/users/{uname}'
    body = requests.get(url, auth=(uname, psswd))
    if body.status_code == 200:
        print(body.json().get('id'))
