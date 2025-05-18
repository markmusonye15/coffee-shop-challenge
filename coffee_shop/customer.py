from __future__ import annotations
from typing import List, Set, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from coffee_shop.order import Order
    from coffee_shop.coffee import Coffee

class Customer:
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
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self) -> List[Order]:
        return self._orders

    def coffees(self) -> Set[Coffee]:
        return {order.coffee for order in self._orders}

    def create_order(self, coffee: Coffee, price: float) -> Order:
        from coffee_shop.order import Order  # Local import to avoid circular import
        order = Order(self, coffee, price)
        return order

    @classmethod
    def most_aficionado(cls, coffee: Coffee) -> Customer:
        if not hasattr(coffee, '_orders') or not coffee.orders():
            return None

        customers: Dict[Customer, float] = {}
        for order in coffee.orders():
            if order.customer in customers:
                customers[order.customer] += order.price
            else:
                customers[order.customer] = order.price

        return max(customers.items(), key=lambda x: x[1])[0]
