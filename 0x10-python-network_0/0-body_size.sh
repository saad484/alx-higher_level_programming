#!/usr/bin/bash
#Display the size of the body of the response
if [ $# -eq 0 ]; then
    echo "Please provide a URL as an argument."
    exit 1
fi
response=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
echo "$response"
