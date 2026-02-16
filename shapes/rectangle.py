from dimension import Width, Height
from shapes.base import Shape


class Rectangle(Shape):
    def __init__(self, width: Width, height: Height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle with width: {self.width} and height {self.height} has an area of  {self.area}"

    @property
    def area(self) -> float:
        return float(self.width) * float(self.height)
