"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()

class Order(StringReprMixin):
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total
    
    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)
    


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        ...

class NoPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value

class FortyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.4)

class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)

class CustomPercent(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)

if __name__ == '__main__':
    five_percent = CustomPercent(5)
    ten_percent = CustomPercent(10)
    twenty_percent = CustomPercent(20)
    thirty_percent = CustomPercent(30)

    forty_percent = FortyPercent()

    order = Order(1000, forty_percent)
    print(order.total, order.total_with_discount)

    fifty_percent = FiftyPercent()
    order_1 = Order(1000, fifty_percent)
    print(order_1.total, order_1.total_with_discount)


    discount_custumized = CustomPercent(30)
    order_discount_custumized = Order(1000, discount_custumized)

    print(order_discount_custumized.total, order_discount_custumized.total_with_discount)

