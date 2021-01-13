import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
      def setUp(self):
          self.customer = Customer("John Wayne", 100.00, 24, 5)
        
        
