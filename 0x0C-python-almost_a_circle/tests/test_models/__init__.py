#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0

    def _init_(self, width=0, height=0):
        self._height = height
        self._width =width
        Rectangle.number_of_instances += 1


 a = Rectangle
 print(a._dic_)
