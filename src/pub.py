class Pub:
    
    def __init__(self, name, till, collection_of_drinks):
        self.name = name 
        self.till = till
        self.collection_of_drinks = collection_of_drinks

    def sell_drink(self, customer, drink):
        customer.buy_drink(drink)

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else: 
            return False