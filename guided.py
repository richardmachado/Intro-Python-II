class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdrawal(self, amount):
        if amount > self.balance:
            return"insufficient funds :("
        self.balance -= amount
        return self.balance


my_account = Account('Richard')

