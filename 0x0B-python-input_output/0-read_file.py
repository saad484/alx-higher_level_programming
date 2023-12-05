#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):

    """print the content of a UTF8 text file to stdout"""
    with open('my_file_0.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    print(data)
