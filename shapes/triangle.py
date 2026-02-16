from dimension import Height, Base
from shapes.base import Shape


class Triangle(Shape):
    def __init__(self, base: Base, height: Height) -> None:
        self.base = base
        self.height = height

    def __str__(self) -> str:
        return f"Triangle with base {self.base} and height {self.height} has an area of {self.area}"

    @property
    def area(self) -> float:
        return 0.5 * float(self.base) * float(self.height)
