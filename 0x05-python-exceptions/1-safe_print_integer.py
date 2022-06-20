#!/usr/bin/python3


def safe_print_integer(value):
    p = False
    try:
        print("{:d}".format(value))
        p = True
    except:
        pass
    return p
