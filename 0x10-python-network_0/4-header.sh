#!/bin/bashi
# Takes URL as an arg, sends a GET request with a header variable X-School-User-Id
curl -s "$1" -X GET -H "X-School-User-Id: 98"
