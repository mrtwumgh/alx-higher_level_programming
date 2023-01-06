#!/usr/bin/python3
"""
A module that prints text
"""


def text_indentation(text):
    """
    A function that prints text with 2 new lines
    after each of these characters ".", "?", ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent = False
    for char in text:
        if char in [".", "?", ":"]:
            print(char)
            print()
            indent = True
        elif char == " " and indent:
            continue
        else:
            print(char, end="")
            indent = False
