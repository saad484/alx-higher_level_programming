#!/usr/bin/python3

"""Define an append to text file function"""

def append_write(filename="", text=""):
    with open(filename, "a", encoding='utf-8') as f:
        """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
        return f.write(text)
