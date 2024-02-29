from ac.BankApplication.InsufficientFundError import InsufficientFundError
from ac.BankApplication.InvalidAmountError import InvalidAmountError
from ac.BankApplication.InvalidPinError import InvalidPinError


class Account:
    def __init__(self, name, acctNumber, pin):
        self.name = name
        self.acctNumber = acctNumber
        self.pin = pin
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def get_account_number(self):
        return self.acctNumber

    def get_balance(self):
        return self.balance

    def withdraw(self, amount, acctPin):
        if amount > self.balance:
            raise InsufficientFundError('Try again when you have enough to withdraw')
        if amount < 0:
            raise InvalidAmountError('Try again when you have')
        if self.pin != acctPin:
            raise InvalidPinError('Try again when you know your pin')
        self.balance -= amount

    def check_Balance(self, acctPin):
        if acctPin == self.pin:
            return self.get_balance()
        else:
            raise InvalidPinError('Are you sure this is your account')

    def __repr__(self):
        return f"{self.name} - {self.get_account_number()}"
