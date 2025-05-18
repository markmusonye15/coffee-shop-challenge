#### Coffee-Shop-Challenge

A comprehensive Python implementation demonstrating object-oriented programming principles with a coffee shop domain featuring Customers, Coffees, and Orders with many-to-many relationships.

### Features
   1.Type Validation: Strict type checking for all model attributes

   2.Immutable Properties: Certain properties cannot be modified after initialization

   3.Relationship Management: Clean handling of many-to-many relationships

   4.Aggregate Methods: Business logic methods like average price calculation

   5.Bonus Features: Advanced querying capabilities

### Models

  .Customer
    
    Responsibilities:

     a.Track customer information

     b.Manage all customer orders

     c.Provide insights into customer preferences

   Attributes:

    - name (string, 1-15 characters, mutable)

 Relationships:

  a.Has many Orders

  b.Has many Coffees through Orders

 Methods:

     a.orders() - Returns all Order instances for this customer

     b.coffees() - Returns unique list of Coffee instances ordered

     c.create_order(coffee, price) - Creates and returns a new Order

     d.most_aficionado(coffee) (classmethod) - Finds top spender for given coffee

. Coffee
   
   Responsibilities:

     a.Track coffee information

     b.Manage all orders for the coffee

     c.Provide sales analytics

 Attributes:

     a.name (string, minimum 3 characters, immutable)

 Relationships:

     a.Has many Orders

     b.Has many Customers through Orders

 Methods:

     a.orders() - Returns all Order instances for this coffee

     b.customers() - Returns unique list of Customer instances

     c.num_orders() - Returns total count of orders

     d.average_price() - Returns mean order price

. Order
 Responsibilities:

     a.Link Customers and Coffees
 
     b.Track transaction details

     c.Enforce business rules

 Attributes:

     a.customer (Customer instance)

     b.coffee (Coffee instance)

     c.price (float, 1.0-10.0, immutable)

 Validation Rules:

     a.Price must be float type

     b.Must be between 1.0 and 10.0 inclusive

     c.Cannot be changed after initialization

     
### Testing
The project includes comprehensive unit tests. To run them:


Run python -m pytest tests/ -v
Test coverage includes:

  .Model initialization and validation

  .Relationship management

  .Aggregate methods

  .Edge cases

### Dependencies
Python 3.8+

pytest (for testing)

### License
MIT License. See LICENSE for details.

This implementation demonstrates clean object-oriented design with:

Proper encapsulation

Clear separation of concerns

Maintainable relationship management

Business logic encapsulation

Comprehensive validation

Perfect for learning intermediate Python concepts or as a foundation for a coffee shop management system!

