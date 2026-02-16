from math import pi

from dimension import Radius
from shapes.base import Shape


class Circle(Shape):
    def __init__(self, radius: Radius) -> None:
        self.radius = radius

    def __str__(self) -> str:
        return f"Circle with radius: {self.radius} has an area of {self.area:.2f}"

    @property
    def area(self) -> float:
        return pi * (float(self.radius) ** 2)
