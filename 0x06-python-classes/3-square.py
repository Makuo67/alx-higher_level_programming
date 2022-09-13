#!/usr/bin/python3
"""Creating a class Square"""


class Square:
    """Class square based on 0-square.py"""

    def __init__(self, size=0):
        """Initializing square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        area = self.__size**2
        return area
