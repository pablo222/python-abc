from dimension import Width
from shapes.base import Shape


class Square(Shape):
    def __init__(self, width: Width) -> None:
        self.width = width

    def __str__(self) -> str:
        return f"Square with width: {self.width.value} has an area of {self.area:.2f}"

    @property
    def area(self) -> float:
        return float(self.width) ** 2
