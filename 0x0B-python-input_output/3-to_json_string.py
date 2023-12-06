#!/usr/bin/python3
import json
'''Define a function the return the json representation of an object'''


def to_json_string(my_obj):
    """Return the json representition of string object"""
    return json.dumps(my_obj)
