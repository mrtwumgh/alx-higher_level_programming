#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        count = 0
        for n in new_list:
            print("{}".format(n), end="")
            count += 1
        print()
        return count
    except NameError:
        return None
