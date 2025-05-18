import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

class TestCustomer:
    """Test suite for Customer class"""
    
    def test_name_validation(self):
        """Test name property validation"""
        # Valid names
        customer1 = Customer("Alice")
        customer2 = Customer("Bob Smith")
        
        assert customer1.name == "Alice"
        assert customer2.name == "Bob Smith"
        
        # Test type validation
        with pytest.raises(TypeError):
            Customer(123)  # Not a string
        with pytest.raises(TypeError):
            Customer(None)  # None type
            
        # Test length validation
        with pytest.raises(ValueError):
            Customer("")  # Too short
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLongForTheLimit")  # Too long
    
    def test_orders_relationship(self):
        """Test customer-order relationship"""
        customer = Customer("Charlie")
        coffee = Coffee("Espresso")
        order1 = Order(customer, coffee, 3.5)
        order2 = Order(customer, coffee, 4.0)
        
        assert len(customer.orders()) == 2
        assert order1 in customer.orders()
        assert order2 in customer.orders()
        assert customer.orders()[0].price == 3.5
    
    def test_coffees_relationship(self):
        """Test customer-coffee relationship"""
        customer = Customer("Diana")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Cappuccino")
        
        Order(customer, coffee1, 4.0)
        Order(customer, coffee1, 4.5)  # Same coffee
        Order(customer, coffee2, 5.0)  # Different coffee
        
        coffees = customer.coffees()
        assert len(coffees) == 2  # Should be unique
        assert coffee1 in coffees
        assert coffee2 in coffees
    
    def test_create_order_method(self):
        """Test create_order method"""
        customer = Customer("Eve")
        coffee = Coffee("Americano")
        
        order = customer.create_order(coffee, 3.5)
        assert isinstance(order, Order)
        assert order in customer.orders()
        assert order.coffee == coffee
        assert order.price == 3.5
        
        # Test price validation
        with pytest.raises(ValueError):
            customer.create_order(coffee, 0.9)  # Below minimum
        with pytest.raises(ValueError):
            customer.create_order(coffee, 10.1)  # Above maximum
    
    def test_most_aficionado_classmethod(self):
        """Test most_aficionado class method"""
        coffee = Coffee("Special Blend")
        customer1 = Customer("Frank")
        customer2 = Customer("Grace")
        
        # Customer1 spends more in total
        Order(customer1, coffee, 6.0)
        Order(customer1, coffee, 5.0)  # Total: 11.0
        Order(customer2, coffee, 5.5)  # Total: 5.5
        
        top_customer = Customer.most_aficionado(coffee)
        assert top_customer == customer1
        
        # Test with no orders
        new_coffee = Coffee("New Blend")
        assert Customer.most_aficionado(new_coffee) is None