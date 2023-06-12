#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
    len_s = len(sentence)
    return len_s, sentence[0]
