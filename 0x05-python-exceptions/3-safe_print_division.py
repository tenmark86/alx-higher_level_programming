#!/usr/bin/python3


def safe_print_division(a, b):
    p = 0
    c = 0.0
    try:
        c = a / b
        p = 1
    except:
        pass
    finally:
        if p == 1:
            print("Inside result: {}".format(c))
            return c
        else:
            print("Inside result: {}".format("None"))
