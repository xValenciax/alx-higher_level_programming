#!/usr/bin/python3
"""this is a module that defines the Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes an instance of the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    @property
    def width(self):
        """returns the value of width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width attribute"""
        self.__width = self.validate_attribute('width', value)

    @property
    def height(self):
        """gets the value of height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height attribute"""
        self.__height = self.validate_attribute('height', value)

    @property
    def x(self):
        """gets the value of x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x attribute"""
        self.__x = self.validate_attribute('x', value)

    @property
    def y(self):
        """gets the value of y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y attribute"""
        self.__y = self.validate_attribute('y', value)

    def validate_attribute(self, name, value) -> int:
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

        if name in ['width', 'height'] and value <= 0:
            raise ValueError('{} must be > 0'.format(name))

        elif name in ['x', 'y'] and value < 0:
            raise ValueError('{} must be >= 0'.format(name))

        return value

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(' ', end='')
            for _ in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            values = [None, None, None, None, None]
            for i, arg in enumerate(args):
                values[i] = arg

            if not isinstance(args[0], int) and args[0] is not None:
                raise TypeError('id must be integer')
            self.id = self.id if values[0] is None else values[0]
            self.width = self.width if values[1] is None else values[1]
            self.height = self.height if values[2] is None else values[2]
            self.x = self.x if values[3] is None else values[3]
            self.y = self.y if values[4] is None else values[4]

        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if not isinstance(value, int) and value is not None:
                        raise TypeError('id must be integer')
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
