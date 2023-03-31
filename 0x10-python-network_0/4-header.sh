#!/bin/bashi
# Takes URL as an arg, sends a GET request with a header variable X-School-User-Id
# must be sent with the value 98 to the URL, and displays response
curl -sH "X-School-User-Id: 98" "$1"

