from __future__ import annotations
from typing import List, Set, TYPE_CHECKING

if TYPE_CHECKING:
    from coffee_shop.order import Order
    from coffee_shop.customer import Customer

class Coffee:
    def __init__(self, name: str):
        self.name = name
        self._orders: List[Order] = []

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

    def orders(self) -> List[Order]:
        return self._orders

    def customers(self) -> Set[Customer]:
        return {order.customer for order in self._orders}

    def num_orders(self) -> int:
        return len(self._orders)

    def average_price(self) -> float:
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)
