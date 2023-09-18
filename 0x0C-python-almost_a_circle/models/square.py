#!/usr/bin/python3
"""this is a module that defines the Rectangle Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size=0, x=0, y=0, id=None):
        """initializes an instances of the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
