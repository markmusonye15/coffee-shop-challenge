from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order


if __name__ == '__main__':
    
    c1 = Customer("Alice")
    c2 = Customer("Bob")

    
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Cappuccino")

    
    o1 = Order(c1, coffee1, 5.0)
    o2 = Order(c1, coffee2, 4.5)
    o3 = Order(c2, coffee1, 6.0)

    
    print(f"{c1.name}'s orders: {[o.coffee.name for o in c1.orders()]}")
    print(f"{coffee1.name}'s customers: {[c.name for c in coffee1.customers()]}")
    print(f"Latte average price: {coffee1.average_price()}")
    print(f"Latte total orders: {coffee1.num_orders()}")

    
    top_customer = Customer.most_aficionado(coffee1)
    print(f"Top customer for Latte: {top_customer.name if top_customer else 'None'}")