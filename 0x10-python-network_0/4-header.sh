#!/bin/bashi
# Takes URL as an arg, sends a GET request with a header variable X-School-User-Id
curl -sH "X-School-User-Id: 98" "$1"
