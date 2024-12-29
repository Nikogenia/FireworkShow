# IMPORTS
from math import sqrt


# CLASSES

# Vector error
class VectorError(Exception):
    pass


# Integer Vector
class Vector(tuple):

    # CONSTRUCTOR
    def __new__(cls, x: int, y: int):

        # If x or y is not an integer, raise an error
        if not isinstance(x, int) or not isinstance(y, int):
            raise VectorError("x and y must be an integer! Use a 'FVector' for float values ...")

        # Return a new vector instance
        return tuple.__new__(cls, (x, y))


    # PROPERTIES

    # X
    @property
    def x(self) -> int:
        return self[0]

    # Y
    @property
    def y(self) -> int:
        return self[1]

    # XX
    @property
    def xx(self) -> tuple[int, int]:
        return self[0], self[0]

    # YY
    @property
    def yy(self) -> tuple[int, int]:
        return self[1], self[1]

    # XY
    @property
    def xy(self) -> tuple[int, int]:
        return self[0], self[1]

    # YX
    @property
    def yx(self) -> tuple[int, int]:
        return self[1], self[0]


    # OVERRIDE METHODS

    # String
    def __str__(self):
        return f"Vector[{self.x}|{self.y}|ID={id(self)}]"

    # Addition
    def __add__(self, other):
        return Vector(self.x + other[0], self.y + other[1])

    # Subtraction
    def __sub__(self, other):
        return Vector(self.x - other[0], self.y - other[1])

    # Multiplication
    def __mul__(self, factor):
        return Vector(self.x * factor, self.y * factor)

    # Division
    def __truediv__(self, divisor):
        return Vector(round(self.x / divisor), round(self.y / divisor))

    # Floor division
    def __floordiv__(self, divisor):
        return Vector(self.x // divisor, self.y // divisor)

    # Modulo
    def __mod__(self, divisor):
        return Vector(self.x % divisor, self.y % divisor)


    # METHODS

    # Update x
    def update_x(self, value: int):
        return Vector(self.x + value, self.y)

    # Update y
    def update_y(self, value: int):
        return Vector(self.x, self.y + value)

    # Length
    def length(self) -> float:
        return round(sqrt(self.x ** 2 + self.y ** 2), 5)

    # Length squared
    def length_squared(self) -> float:
        return self.x ** 2 + self.y ** 2

    # Distance
    def distance(self, other) -> float:
        return round(sqrt((self.x - other[0]) ** 2 + (self.y - other[1]) ** 2), 5)

    # Distance squared
    def distance_squared(self, other) -> int:
        return abs(self.x - other[0]) + abs(self.y - other[1])

    # Normalize
    def normalize(self, ignore_zero_length: bool = False):
        if self.length() == 0:
            if ignore_zero_length:
                return Vector(0, 0)
            raise VectorError("Cannot normalize a vector with length 0!")
        return Vector(round(self.x / self.length()), round(self.y / self.length()))

    # Is normalized
    def is_normalized(self) -> bool:
        return round(self.length()) == 1

    # Float
    def float(self):
        from .fvector import FVector
        return FVector(self.x, self.y)
