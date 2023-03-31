#!/usr/bin/python3
# A Script that takes in URL, sends a request, and displays the value of
# a variable in the header
from urllib import request
import sys


with request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
