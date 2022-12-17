#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_mapping = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]

    result = 0
    index = 0
    while index < len(roman_string):
        found = False
        for roman, integer in roman_to_int_mapping:
            if roman_string[index:index+len(roman)] == roman:
                result += integer
                index += len(roman)
                found = True
                break
        if not found:
            return 0
    return result
