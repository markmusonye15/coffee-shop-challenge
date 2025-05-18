import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer
from coffee_shop.order import Order

class TestCoffee:
    """Test suite for Coffee class"""
    
    def test_coffee_initialization(self):
        """Test Coffee initialization with valid name"""
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
    
    def test_name_validation(self):
        """Test name validation rules"""
        # Test valid names
        Coffee("Esp")  # Minimum length
        Coffee("Cappuccino")  # Normal case
        
        # Test invalid names
        with pytest.raises(TypeError):
            Coffee(123)  # Not a string
            
        with pytest.raises(ValueError):
            Coffee("A")  # Too short
    
    def test_name_immutability(self):
        """Test that name cannot be changed after initialization"""
        coffee = Coffee("Mocha")
        
        with pytest.raises(AttributeError):
            coffee.name = "New Name"
    
    def test_orders_property(self):
        """Test orders property returns correct orders"""
        coffee = Coffee("Flat White")
        customer = Customer("Frank")
        order1 = Order(customer, coffee, 4.0)
        order2 = Order(customer, coffee, 4.5)
        
        assert len(coffee.orders()) == 2
        assert order1 in coffee.orders()
        assert order2 in coffee.orders()
        assert coffee.orders()[0].price == 4.0
        assert coffee.orders()[1].price == 4.5
    
    def test_customers_property(self):
        """Test customers property returns unique customers"""
        coffee = Coffee("Macchiato")
        customer1 = Customer("Grace")
        customer2 = Customer("Henry")
        
        # Create orders - some from same customer
        Order(customer1, coffee, 3.5)
        Order(customer1, coffee, 4.0)  # Same customer again
        Order(customer2, coffee, 4.5)  # Different customer
        
        customers = coffee.customers()
        assert len(customers) == 2  # Should be unique
        assert customer1 in customers
        assert customer2 in customers
    
    def test_num_orders(self):
        """Test num_orders method"""
        coffee = Coffee("Cold Brew")
        assert coffee.num_orders() == 0  # Initially zero
        
        customer = Customer("Ivy")
        Order(customer, coffee, 4.5)
        assert coffee.num_orders() == 1
        
        Order(customer, coffee, 5.0)
        assert coffee.num_orders() == 2
    
    def test_average_price(self):
        """Test average_price calculation"""
        coffee = Coffee("Pour Over")
        customer = Customer("Jack")
        
        # Test with no orders
        assert coffee.average_price() == 0
        
        # Test with one order
        Order(customer, coffee, 5.0)
        assert coffee.average_price() == 5.0
        
        # Test with multiple orders
        Order(customer, coffee, 7.0)
        assert coffee.average_price() == 6.0  # (5+7)/2
        
        Order(customer, coffee, 8.0)
        assert coffee.average_price() == pytest.approx(6.666666666666667)  # (5+7+8)/3
    
    def test_average_price_with_zero_orders(self):
        """Test average_price returns 0 when no orders exist"""
        coffee = Coffee("Decaf")
        assert coffee.average_price() == 0