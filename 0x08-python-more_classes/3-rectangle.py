#!/usr/bin/python3

"""defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        if self.width == 0 or self.height == 0:
            return ""

        rect_list = []

        for i in range(self.height):
            for j in range(self.width):
                rect_list.append('#')
            rect_list.append('\n')
        rect_list.pop(-1)
        return ''.join(rect_list)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
