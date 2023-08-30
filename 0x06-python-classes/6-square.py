#!/usr/bin/python3\

"""This a Module that contains one class called Square"""


class Square:
    """Represents a Square, but it's empty for now"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property that returns the size"""
        return self.__size

    @property
    def position(self):
        """property that returns the position"""
        return self.__position

    @size.setter
    def size(self, size):
        """property that sets the size"""
        if not str(type(size)).__contains__('int'):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @position.setter
    def position(self, pos):
        """property that sets the position"""
        if not isinstance(pos, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(pos) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(pos[0], int) and not isinstance(pos[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif pos[0] < 0 or pos[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = pos

    def area(self):
        """method that calculates the area and return it"""
        return self.__size ** 2

    def my_print(self):
        """method that prints the square"""
        if not self.__size:
            print()
            return

        for k in range(0, self.__position[1]):
            print()

        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(' ', end='')
            for x in range(0, self.__size):
                print('#', end='')
            print()
