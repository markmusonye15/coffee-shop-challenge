from __future__ import annotations
from typing import List, Set

class Customer:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self) -> List['Order']:
        from .order import Order  # Local import
        return [order for order in Order.all if order.customer == self]

    def coffees(self) -> Set['Coffee']:
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee: 'Coffee', price: float) -> 'Order':
        from .order import Order  # Local import
        return Order(self, coffee, price)