#!/usr/bin/python3
""" Script takes in URL, sends a request, and displays the 
value of a variable.
"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
