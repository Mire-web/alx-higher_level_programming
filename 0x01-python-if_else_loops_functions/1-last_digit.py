#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_number = abs(number) % 10

if number < 0:
    abs_number *= -1

if abs_number > 5:
    print(f'Last digit of {number} is {abs_number} and is greater than 5')
elif (number % 10) == 0:
    print(f'Last digit of {number} is {abs_number} and is zero')
elif (abs_number % 10) < 6 and (abs_number) != 0:
    print(f'Last digit of {number} is {abs_number} and is less than 6 and not 0')
