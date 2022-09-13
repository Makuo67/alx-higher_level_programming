#!/usr/bin/python3
"""Creating a class Square"""


class Square:
    """Class square based on 0-square.py"""
    def __init__(self, size=0):
        self.__size = size
        if size is not type(int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
