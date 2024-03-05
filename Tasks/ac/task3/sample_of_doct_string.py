from decimal import Decimal

from ac.BankApplication.Account import Account


class Account:
    """THis class represents an account that"""
    >>> account =Account('mavell', Decimal('25.0'))
    >>> account.name
    >>> account.balance
    help(Account)

    def __init__(self,name,balance:Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)