#!/bin/bash
# prints out the Content_Length of the a given url
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
