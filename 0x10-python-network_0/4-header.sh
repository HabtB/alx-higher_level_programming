#!/bin/bash
# Takes in a URL as an argument, sends a GET request with 
# A header variable X-School-User-Id must be sent with the value 98
# to the URL, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"

