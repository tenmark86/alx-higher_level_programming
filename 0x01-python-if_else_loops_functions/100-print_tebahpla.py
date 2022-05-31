#!/usr/bin/python3
for i in range(122, 96, -2):
    print("{:c}{:c}".format(i, (i - 1) - 32), end="")
