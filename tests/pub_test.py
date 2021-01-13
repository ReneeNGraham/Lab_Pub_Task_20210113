import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        # self.drink_1 = Drink("Martini", 7, 2)
        # self.drink_2 = Drink("Beer", 4, 3)
        # self.drink_3 = Drink("Cocktail", 8, 2)
        self.pub = Pub("Pracing Ponies",0, 10)
        # self.customer = Customer("Johnny Bravo", 20, 4)
        # drinks = [self.drink_1, self.drink_2, drink_3]