#!/bin/bash

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLS"

