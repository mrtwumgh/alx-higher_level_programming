#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    for i in my_list:
        new_set.add(i)
    result = sum(new_set)
    return result
