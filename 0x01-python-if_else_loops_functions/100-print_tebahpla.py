#!/usr/bin/python3
print("".join(
    "{}".format(chr(c) if c % 2 == 0 else chr(c - 32))
    for c in range(122, 96, -1)
    ), end="")
