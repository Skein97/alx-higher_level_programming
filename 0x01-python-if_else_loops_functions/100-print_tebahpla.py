#!/usr/bin/python3
for ch in reversed(range(97, 123)):
    print(f"{(ch if (ch % 2 == 0) else (ch - 32)):c}", end='')
