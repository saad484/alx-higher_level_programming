#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """print the content of a UTF8 text file to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
