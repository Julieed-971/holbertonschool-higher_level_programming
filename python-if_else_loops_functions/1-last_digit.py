#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = number % -10
else:
    n = number % 10
if n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
if n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n < 6:
    print(f"Last digit of {number} is {n} and is less then 6 and not 0")
