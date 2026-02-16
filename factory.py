from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, **kwargs):
        shape_type = shape_type.lower()

        if shape_type == "circle":
            return Circle(kwargs["radius"])
        elif shape_type == "square":
            return Square(kwargs["width"])
        elif shape_type == "rectangle":
            return Rectangle(kwargs["width"], kwargs["height"])
        elif shape_type == "triangle":
            return Triangle(kwargs["base"], kwargs["height"])
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
