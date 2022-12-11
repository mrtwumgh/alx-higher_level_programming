#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    num_args = len(sys.argv)
    print("{} arguments:".format(num_args - 1))
    if num_args > 0:
        for i, args in enumerate(sys.argv):
            if args == (sys.argv[0]):
                continue
            print("{}: {}".format(i, args))
    else:
        print(".")
