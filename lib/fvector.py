# IMPORTS
from math import sqrt


# CLASSES

# Vector error
class VectorError(Exception):
    pass


# Float Vector
class FVector(tuple):

    # CONSTRUCTOR
    def __new__(cls, x: int | float, y: int | float):

        # If x or y is not an integer or float, raise an error
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise VectorError("x and y must be a float or integer!")

        # Return a new vector instance
        return tuple.__new__(cls, (float(x) if isinstance(x, int) else round(x, 5), float(y) if isinstance(y, int) else round(y, 5)))


    # PROPERTIES

    # X
    @property
    def x(self) -> float:
        return self[0]

    # Y
    @property
    def y(self) -> float:
        return self[1]

    # XX
    @property
    def xx(self) -> tuple[float, float]:
        return self[0], self[0]

    # YY
    @property
    def yy(self) -> tuple[float, float]:
        return self[1], self[1]

    # XY
    @property
    def xy(self) -> tuple[float, float]:
        return self[0], self[1]

    # YX
    @property
    def yx(self) -> tuple[float, float]:
        return self[1], self[0]


    # OVERRIDE METHODS

    # String
    def __repr__(self):
        return f"FVector[{self.x}|{self.y}|ID={id(self)}]"

    # Addition
    def __add__(self, other):
        return FVector(self.x + other[0], self.y + other[1])

    # Subtraction
    def __sub__(self, other):
        return FVector(self.x - other[0], self.y - other[1])

    # Multiplication
    def __mul__(self, factor):
        return FVector(self.x * factor, self.y * factor)

    # Division
    def __truediv__(self, divisor):
        return FVector(self.x / divisor, self.y / divisor)

    # Floor division
    def __floordiv__(self, divisor):
        return FVector(self.x // divisor, self.y // divisor)

    # Modulo
    def __mod__(self, divisor):
        return FVector(self.x % divisor, self.y % divisor)


    # METHODS

    # Update x
    def update_x(self, value: float):
        return FVector(self.x + value, self.y)

    # Update y
    def update_y(self, value: float):
        return FVector(self.x, self.y + value)

    # Length
    def length(self) -> float:
        return round(sqrt(self.x ** 2 + self.y ** 2), 5)

    # Length squared
    def length_squared(self) -> float:
        return round(self.x ** 2 + self.y ** 2, 5)

    # Distance
    def distance(self, other) -> float:
        return round(sqrt((self.x - other[0]) ** 2 + (self.y - other[1]) ** 2), 5)

    # Distance squared
    def distance_squared(self, other) -> float:
        return round(abs(self.x - other[0]) + abs(self.y - other[1]), 5)

    # Normalize
    def normalize(self, ignore_zero_length: bool = False):
        if self.length() == 0:
            if ignore_zero_length:
                return FVector(0, 0)
            raise VectorError("Cannot normalize a vector with length 0!")
        return FVector(self.x / self.length(), self.y / self.length())

    # Is normalized
    def is_normalized(self) -> bool:
        return self.length() == 1

    # Integer
    def int(self):
        from .vector import Vector
        return Vector(round(self.x), round(self.y))
