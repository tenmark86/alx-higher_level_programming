#!/usr/bin/python3
"""
Finds a peak
"""


def find_peak(list_of_integers):
    """Find peak in unsorted list"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
