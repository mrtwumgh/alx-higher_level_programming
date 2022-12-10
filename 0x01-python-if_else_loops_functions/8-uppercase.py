#!/usr/bin/python3
def uppercase(str):
    string = ""
    for char in str:
        if (ord(char) >= 97) and (ord(char) <= 122):
            string += chr(ord(char) - 32)
        else:
            string += char

    print(string)
