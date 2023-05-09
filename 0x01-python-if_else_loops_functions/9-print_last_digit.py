#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_digit = number % 10
    else:
        l_digit = number % -10
        l_digit *= -1

    print(f"{l_digit:d}", end='')
    return (l_digit)
