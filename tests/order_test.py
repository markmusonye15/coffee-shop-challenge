import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee_shop.order import Order
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

class TestOrder:
    """Test suite for Order class"""
    
    def test_order_initialization(self):
        """Test proper order initialization"""
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 5.0
    
    def test_price_validation(self):
        """Test price validation rules"""
        customer = Customer("Bob")
        coffee = Coffee("Espresso")
        
        # Valid prices
        Order(customer, coffee, 1.0)  # Minimum
        Order(customer, coffee, 5.5)  # Middle
        Order(customer, coffee, 10.0)  # Maximum
        
        # Invalid prices
        with pytest.raises(TypeError):
            Order(customer, coffee, "5")  # Not a float
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.9)  # Below minimum
        with pytest.raises(ValueError):
            Order(customer, coffee, 10.1)  # Above maximum
    
    def test_price_immutability(self):
        """Test price cannot be changed after initialization"""
        customer = Customer("Charlie")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 4.5)
        
        with pytest.raises(AttributeError):
            order.price = 5.0
    
    def test_customer_property(self):
        """Test customer property validation"""
        coffee = Coffee("Mocha")
        
        # Valid customer
        customer = Customer("Diana")
        Order(customer, coffee, 3.5)
        
        # Invalid customer
        with pytest.raises(TypeError):
            Order("Not a customer", coffee, 3.5)
    
    def test_coffee_property(self):
        """Test coffee property validation"""
        customer = Customer("Eve")
        
        # Valid coffee
        coffee = Coffee("Americano")
        Order(customer, coffee, 4.0)
        
        # Invalid coffee
        with pytest.raises(TypeError):
            Order(customer, "Not a coffee", 4.0)
    
    def test_relationship_management(self):
        """Test order properly registers with customer and coffee"""
        customer = Customer("Frank")
        coffee = Coffee("Flat White")
        order = Order(customer, coffee, 4.5)
        
        # Verify relationships
        assert order in customer.orders()
        assert order in coffee.orders()
        assert coffee in customer.coffees()
        assert customer in coffee.customers()