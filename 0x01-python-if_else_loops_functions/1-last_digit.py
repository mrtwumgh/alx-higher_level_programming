#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10

digit_5 = "Last digit of {:d} is {:d} and is greater than 5"
digit_0 = "Last digit of {:d} is {:d} and is zero"
digit_6 = "Last digit of {:d} is {:d} and is less than 6 and not 0"

if last_digit > 5:
    print(digit_5.format(number, last_digit))
elif last_digit == 0:
    print(digit_0.format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print(digit_6.format(number, last_digit))
