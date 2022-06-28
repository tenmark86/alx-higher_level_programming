able File  14 lines (10 sloc)  262 Bytes

#!/usr/bin/python3
"""
Module for a class that prevents dynamic attributes creation
"""


class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
