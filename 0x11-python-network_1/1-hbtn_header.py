#!/usr/bin/python3
# A Script that takes in URL, sends a request, and displays the value of
# a variable in the header
from urllib import request
import sys


url = sys.argv[1]

req = request.Request(url)
with request.urlopen(req) as response:
    headers = response.info()
    x_request_id = headers.get('X-Request-Id')
    print(f"{x_request_id}")
