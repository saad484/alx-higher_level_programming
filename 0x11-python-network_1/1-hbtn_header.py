#!/usr/bin/python3
"""
Python script that takes in a url, sends a request and
Displays The values of X-Request-Id variable found
in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
