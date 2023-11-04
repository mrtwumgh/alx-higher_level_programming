#!/usr/bin/python3
"""
module that prints text with 2 newlines
"""


def text_indentation(text):
    """
    function that prints text with 2 newlines
    after each of these characters .,? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in ['.', '?', ':']:
        text = text.replace(char, char + '\n\n')
    lines = text.split('\n')
    lines = [line.strip() for line in lines]
    text = '\n'.join(lines)

    print(text)
