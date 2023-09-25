#!/usr/bin/python3
"""this is a module that defines the Rectangle Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size=0, x=0, y=0, id=None):
        """initializes an instances of the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns the string representation of an obj
        """
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        gets the value of size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the value of size attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates an existing object's attributes
        """
        if args is not None and len(args) != 0:
            values = [None, None, None, None]
            for i, arg in enumerate(args):
                values[i] = arg

            if not isinstance(args[0], int) and args[0] is not None:
                raise TypeError('id must be integer')
            self.id = self.id if values[0] is None else values[0]
            self.size = self.size if values[1] is None else values[1]
            self.x = self.x if values[2] is None else values[2]
            self.y = self.y if values[3] is None else values[3]

        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if not isinstance(value, int) and value is not None:
                        raise TypeError('id must be integer')
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of an obj
        """
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
