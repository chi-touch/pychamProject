from ac.BankApplication.InsufficientFundError import InsufficientFundError


class Account:
    def __init__(self, name, acctNumber, pin):
        self.name = name
        self.acctNumber = acctNumber
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def withdraw(self,amount,acctPin):
            if amount > self.balance:
                raise InsufficientFundError('Try again when you have enough to withdraw')
            self.balance -= amount

    def checkBalance(self,acctPin):
        return self.balance


