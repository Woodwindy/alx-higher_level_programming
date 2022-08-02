#!/usr/bin/python3
"""A function that iherits from list"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))

