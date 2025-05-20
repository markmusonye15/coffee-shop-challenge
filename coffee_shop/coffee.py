from __future__ import annotations
from typing import List, Set

class Coffee:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed after initialization")
        self._name = value

    def orders(self) -> List['Order']:
        from .order import Order  # Local import
        return [order for order in Order.all if order.coffee == self]

    def customers(self) -> Set['Customer']:
        return list({order.customer for order in self.orders()})

    def num_orders(self) -> int:
        return len(self.orders())

    def average_price(self) -> float:
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0