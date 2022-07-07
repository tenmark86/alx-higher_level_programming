#!/usr/bin/python3
"""
Define a square class from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation a scuare"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a scuare
        Args: size, id, x, y
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get,setter of size to square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Check corrects attribures"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, var in kwargs.items():
                if key == "id":
                    if var is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = var
                elif key == "size":
                    self.size = var
                elif key == "x":
                    self.x = var
                elif key == "y":
                    self.y = var

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
