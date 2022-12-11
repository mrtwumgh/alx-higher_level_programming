#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num_args = len(sys.argv)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args - 1))

    if num_args > 0:
        for i, arg in range(1, sys.argv):
            if i == 0:
                continue
            print("{}: {}".format(i, arg))
    else:
        print(".")
