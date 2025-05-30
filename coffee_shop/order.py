from __future__ import annotations
from typing import TYPE_CHECKING

class Order:
    all: list['Order'] = []

    def __init__(self, customer: 'Customer', coffee: 'Coffee', price: float):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed after initialization")
        self._price = value

    @property
    def customer(self) -> 'Customer':
        return self._customer

    @customer.setter
    def customer(self, value: 'Customer') -> None:
        
        from .customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self) -> 'Coffee':
        return self._coffee

    @coffee.setter
    def coffee(self, value: 'Coffee') -> None:
        
        from .coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = value