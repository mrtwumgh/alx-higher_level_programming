#!/usr/bin/python3
"""
A module that manipulates text
"""


def text_indentation(text):
    """
    prints 2 new lines after these
    characters: '.', '?', ':'

    Args:
        text: string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ".,?,:"
    i = 0
    text = text.strip()
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] == "\n" or text[i] in chars:
            if text[i] in chars:
                print()
                print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
