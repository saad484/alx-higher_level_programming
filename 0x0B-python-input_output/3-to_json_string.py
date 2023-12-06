#!/usr/bin/python3
'''Define a function the return the json representation of an object'''
import json


def to_json_string(my_obj):
    """Return the json representition of string object"""
    return json.dumps(my_obj)
