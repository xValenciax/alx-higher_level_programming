#!/usr/bin/python3\

"""This a Module that contains one class called Square"""


class Square:
    """Represents a Square, but it's empty for now"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if not str(type(size)).__contains__('int'):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position.count < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(position[0], int) and not isinstance(position[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        return self.size ** 2

    def my_print(self):
        if not self.size:
            print()
            return

        for k in range(self.position[1]):
            print()

        for i in range(self.area()):
            if (i + 1) % self.size == 1:
                for j in range(self.position[0]):
                    print('_', end='')

            print('#', end='')
            if (i + 1) % self.size == 0:
                print()
