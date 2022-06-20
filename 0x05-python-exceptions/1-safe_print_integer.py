#!/usr/bin/python3
def safe_print_integer(value):
    try:
            print("{:d}".format(value))
            result = True
    except ValueError:
        result = False
    except TypeError:
        result = False
    return result
