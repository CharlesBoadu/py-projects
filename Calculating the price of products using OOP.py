class Product:

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, num_of_items_to_be_bought):
        if num_of_items_to_be_bought < 10:
            return num_of_items_to_be_bought * self.price
        elif num_of_items_to_be_bought > 10 and num_of_items_to_be_bought < 99:
            return num_of_items_to_be_bought * self.price * 0.10
        elif num_of_items_to_be_bought >= 100:
            return num_of_items_to_be_bought * self.price * 0.20

    def make_purchase(self, num_of_items_to_be_bought):
        return num_of_items_to_be_bought/100 * self.price

e = Product('Apple', 20, 10)
print("The cost of Apple is ${:.2f}".format(e.get_price(7)))

        
