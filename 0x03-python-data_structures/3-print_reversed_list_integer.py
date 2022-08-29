#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for numbers in my_list:
        numbers = my_list.pop()
        print("{:d}".format(numbers))
