#!/usr/bin/python3
"""
Defines a rectancle
"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """Instantiation of width and height"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2
