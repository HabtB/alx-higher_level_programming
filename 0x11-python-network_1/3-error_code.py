#!/usr/bin/python3
"""A script, takes in URL,sends a request, and displays the response"""
from urllib import request, error
from urllib import error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
