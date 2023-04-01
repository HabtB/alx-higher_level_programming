#!/usr/bin/python3
""" 
A script that takes github credentials and uses the GitHubAPI
to display id
"""
import sys
import requests

if __name__ == "__main__":
    uname = sys.argv[1]
    token = sys.argv[2]
    headers = {'Authorization': 'token {}'.format(token)}
    url = 'https://api.github.com/user'
    body = requests.get(url, headers=headers)
    if body.status_code == 200:
        print((body.json()).get('id'))
