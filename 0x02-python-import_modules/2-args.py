#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    if num == 1:
        print("{:d} argument:".format(num))
        for i in range(len(argv) - 1):
            print("{:d}: {}".format(i + 1, argv[i + 1]))
    elif num > 1:
        print("{:d} arguments:".format(num))
        for i in range(len(argv) - 1):
            print("{:d}: {}".format(i + 1, argv[i + 1]))
    else:
        print("{} arguments.".format(num))
