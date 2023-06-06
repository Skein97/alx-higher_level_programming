#!/usr/bin/python3

"""Module for magic_string function"""


def magic_string(my_list=[]):
    """returns “BestSchool” n times the number of the iteration"""
    my_list += ["BestSchool"]
    return ", ".join(my_list)
