#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = 32
        else:
            num = 0
        print(f"{(ord(str[i]) - num):c}", end='')
    return pass