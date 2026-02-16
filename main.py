from factory import ShapeFactory


def main():
    shape_data = {
        "shape_type": "circle",
        "radius": 5
    }
    shape_circle = ShapeFactory.create_shape(**shape_data)
    print(shape_circle)

    shape_data_rectangle = {
        "shape_type": "rectangle",
        "width": 10,
        "height": 8,
    }
    shape2 = ShapeFactory.create_shape(**shape_data_rectangle)
    print(shape2)

    shape_data_triangle = {
        "shape_type": "triangle",
        "base": 10,
        "height": 8,
    }
    shape_triangle = ShapeFactory.create_shape(**shape_data_triangle)
    print(shape_triangle)


if __name__ == "__main__":
    main()
