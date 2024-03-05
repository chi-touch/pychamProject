from ac.BankApplication.InsufficientFundError import InsufficientFundError
from ac.BankApplication.InvalidAmountError import InvalidAmountError
from ac.BankApplication.InvalidPinError import InvalidPinError


class Account:
    def __init__(self, name, number, pin):
        self.validate(pin)
        self.name = name
        self.__acctNumber = number
        self.pin = pin
        self.balance = 0

    @staticmethod
    def validate(pin):
        if len(pin) != 4:
            raise InvalidPinError('Pin must be 4 digits long')

    def deposit(self, amount):
        self.balance += amount

    def get_account_number(self):
        return self.__acctNumber

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

    def check_Balance(self, pinNumber):
        if self.pin == pinNumber:
            return self.get_balance()
        else:
            raise InvalidPinError('Are you sure this is your account')

    def __repr__(self):
        return f"{self.name} - {self.get_account_number()}"
