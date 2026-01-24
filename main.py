from abc import ABC, abstractmethod
from math import pi

class PoleFigury(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    @abstractmethod
    def pole_powierzchni(self) -> float:
        pass

class Kwadrat(PoleFigury) :
    def __init__(self, a: float) -> None:
        self.a = a

    def __str__(self) -> str:
        return f"Pole kwadratu o boku {self.a} wynosi {self.pole_powierzchni}"

    @property
    def pole_powierzchni(self) -> float :
        return self.a ** 2


class Prostokat(PoleFigury):
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return  f"Pole prostokatka o boku {self.a} i {self.b} wynosi {self.pole_powierzchni}"

    @property
    def pole_powierzchni(self) -> float :
        return self.a * self.b


class Kolo(PoleFigury):
    def __init__(self, r: float) -> None:
        self.r = r

    def __str__(self) -> str:
        return f"Pole kolo {self.r} wynosi {self.pole_powierzchni}"

    @property
    def pole_powierzchni(self) -> float :
        return pi * (self.r ** 2)


kwadrat = Kwadrat(2)
print(kwadrat)
prostokat = Prostokat(5, 4)
print(prostokat)
kolo = Kolo(5)
print(kolo)
