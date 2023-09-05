#!/usr/bin/python3

"""defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self) -> None:
        """Class Destructor"""
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    def __str__(self) -> str:
        if self.width == 0 or self.height == 0:
            return ""

        rect_list = []

        for i in range(self.height):
            for j in range(self.width):
                rect_list.append(str(self.print_symbol))
            rect_list.append('\n')
        rect_list.pop(-1)
        return ''.join(rect_list)

    def __repr__(self) -> str:
        """return an eval-valid string representation of the class"""
        return 'Rectangle({}, {})'.format(self.width, self.height)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if Rectangle.area(rect_1) >= Rectangle.area(rect_2) else rect_2

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
