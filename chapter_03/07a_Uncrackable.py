# Problem 'Uncrackable' wc17c3j3

from curses.ascii import isdigit

password = input()

lower = 0
upper = 0
digit = 0

if (len(password) >= 8) and (len(password) <= 12):
    for char in password:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char.isdigit():
            digit += 1

if (lower >= 3) and (upper >= 2) and (digit >= 1):
    print('Valid')
else:
    print('Invalid')