#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    num = len(argv) - 1
    operators = ['+', '-', '*', '/']
    if num != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            result = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, result))
        elif argv[2] == '-':
            result = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, result))
        elif argv[2] == '*':
            result = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, result))
        elif argv[2] == '/':
            result = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, result))
