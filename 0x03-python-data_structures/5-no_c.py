#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for x in my_string:
        if x not in ['c', 'C']:
            new_string += x
    return new_string
