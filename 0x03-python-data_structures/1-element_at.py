#!/usr/bin/python3
# Function that retrieves an element from a list like in C.
def element_at(my_list, idx):
    for idx in my_list:
        if idx == -idx:
            print("None")
        elif idx > len(my_list):
            print("None")
        else:
            print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
