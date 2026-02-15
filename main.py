from abc import ABC, abstractmethod
from math import pi
from factory import Width, Height, Radius


class PoleFigury(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    @abstractmethod
    def pole_powierzchni(self) -> float:
        pass

class Kwadrat(PoleFigury) :
    def __init__(self, width: Width) -> None:
        self.width = width

    def __str__(self) -> str:
        return f"Pole kwadratu o boku {self.width.value} wynosi {self.pole_powierzchni:.2f}"

    @property
    def pole_powierzchni(self) -> float :
        return float(self.width) ** 2


class Prostokat(PoleFigury):
    def __init__(self, width: Width, height: Height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return  f"Pole prostokatka o boku {self.width} i {self.height} wynosi {self.pole_powierzchni}"

    @property
    def pole_powierzchni(self) -> float :
        return float(self.width) * float(self.height)


class Kolo(PoleFigury):
    def __init__(self, radius: Radius) -> None:
        self.radius = radius

    def __str__(self) -> str:
        return f"Pole kolo {self.radius} wynosi {self.pole_powierzchni}"

    @property
    def pole_powierzchni(self) -> float :
        return pi * (float(self.radius) ** 2)


kwadrat = Kwadrat(Width(2))
print(kwadrat)
prostokat = Prostokat(5, 4)
print(prostokat)
kolo = Kolo(5)
print(kolo)
