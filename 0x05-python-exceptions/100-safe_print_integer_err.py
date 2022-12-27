#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as ect:
        print("{} is not an integer".format(ect),  file=sys.stderr)
        return False
