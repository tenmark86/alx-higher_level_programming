#!/usr/bin/python3
"""
Defines a function that adds a new attribute to an object if its possible
"""


def add_attribute(obj, att, value):
    """add_attribure: add a new objt
    raise typerror if attribute not added
    """
    if type(obj) is int:
        raise TypeError("can`t add new attribute")

    return att, value
