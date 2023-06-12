#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        character = None
    else:
        character = sentence[0]
    len_s = len(sentence)
    return (len_s, character)
