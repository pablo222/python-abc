class Dimension:
    def __init__(self, value: float):
        self.value = value

    def __float__(self):
        return float(self.value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"


class Width(Dimension):
    pass


class Height(Dimension):
    pass


class Radius(Dimension):
    pass


class Base(Dimension):
    pass
