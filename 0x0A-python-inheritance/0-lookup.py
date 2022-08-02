#!/usr/bin/python3
""" A function that return of available attributes
and methods of an object"""


def lookup(obj):
    """returns list of available
        attributes and methods of an object"""
    return dir(obj)
