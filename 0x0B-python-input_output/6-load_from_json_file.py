#!/usr/bin/python3
"""
Define a function that create an object from a 'json file'
"""


import json


def load_from_json_file(filename):
    """
    create object from a JSON file
    """
    with open(filename) as f:
        return json.load(f)
