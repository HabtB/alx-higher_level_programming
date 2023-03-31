#!/usr/bin/python3
""" A script that fetches a URL, and displays the body"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    body = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(body.text)))
    print("\t- content: {}".format(body.text))
