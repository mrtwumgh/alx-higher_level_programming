#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
       return None
    else:
        for x in sorted(my_list, reverse=True):
            print("{:d}".format(x))
