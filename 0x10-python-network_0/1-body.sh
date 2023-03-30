#!/bin/bash
# Sends a get requrest to a given url and displays only with a 200 status code
curl -s -o /dev/null -w "%{http_code}\n" "$1" | grep -q 200 && curl -s "$1"
