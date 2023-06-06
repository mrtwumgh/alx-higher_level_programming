#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        result += i
    print("{}".format(result))
