from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    @abstractmethod
    def area(self) -> float:
        pass
