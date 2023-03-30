#!/usr/bin/env bash
url=$1

response=$(curl -sI $url)
size=$(echo "$response" | awk '/Content-Length/ {print $2}')
if [[ -n "$size" ]]; then
    echo "$size"
fi
