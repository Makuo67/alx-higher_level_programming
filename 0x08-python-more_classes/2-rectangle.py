#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def width(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        return (width * height)

    def perimeter(self):
        if width == 0 or height == 0:
            return 0
        else:
            return ((width * 2) + (height * 2))