import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Charlie")
        self.coffee = Coffee("Americano")

    def test_valid_order(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_invalid_price_type(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 20.0)  # Out of range
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)   # Too low
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "5.0")  # Not float

if __name__ == '__main__':
    unittest.main()
