import unittest
from customer import Customer
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Alice")
        self.customer2 = Customer("Bob")
        self.espresso = Coffee("Espresso")

    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("A")  # Too short

    def test_orders_and_customers(self):
        self.customer1.create_order(self.espresso, 3.0)
        self.customer2.create_order(self.espresso, 4.0)
        self.assertEqual(self.espresso.num_orders(), 2)
        customers = self.espresso.customers()
        self.assertIn(self.customer1, customers)
        self.assertIn(self.customer2, customers)

    def test_average_price(self):
        self.customer1.create_order(self.espresso, 2.0)
        self.customer2.create_order(self.espresso, 4.0)
        self.assertEqual(self.espresso.average_price(), 3.0)

    def test_average_price_zero(self):
        self.assertEqual(self.espresso.average_price(), 0)

if __name__ == '__main__':
    unittest.main()
