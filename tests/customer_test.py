import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.latte = Coffee("Latte")
        self.mocha = Coffee("Mocha")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("ThisNameIsWayTooLong")

    def test_create_order(self):
        order = self.customer.create_order(self.latte, 4.5)
        self.assertIn(order, self.customer.orders())
        self.assertEqual(order.coffee, self.latte)
        self.assertEqual(order.customer, self.customer)

    def test_coffees_returns_unique(self):
        self.customer.create_order(self.latte, 3.0)
        self.customer.create_order(self.latte, 4.0)
        self.customer.create_order(self.mocha, 5.0)
        self.assertEqual(len(self.customer.coffees())),
