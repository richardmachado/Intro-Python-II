class User:
    def __init__(self, money):
        self.money = money
        self.cart = []


    def __str__(self):
        return f"Money: ${self.money}, Cart: {self.cart}"

    def add_to_cart(self, product):
        self.cart.append(product)
        self.print_cart()

    def print_cart(self):
        print("Your cart contents: ", [(p.name, p.price) for p in self.cart],' \n')
