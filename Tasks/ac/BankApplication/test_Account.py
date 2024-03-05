import unittest

from ac.BankApplication.InsufficientFundError import InsufficientFundError
from ac.BankApplication.InvalidAmountError import InvalidAmountError
from ac.BankApplication.Account import Account
from ac.BankApplication.InvalidPinError import InvalidPinError


class MyTestCase(unittest.TestCase):

    def test_that_account_can_deposit(self):
        account = Account('chichi', '3506856011', '2222')
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_that_amount_can_be_withdrawn(self):
        account = Account('chichi', '3506856011', '2222')
        account.deposit(1000)
        account.withdraw(500, "2222")
        self.assertEqual(account.get_balance(), 500)

    def test_that_amount_greaterThan_balance_cannot_be_withdrawn(self):
        account = Account('chichi', '3506856011', '2222')
        account.deposit(1000)
        with self.assertRaises(InsufficientFundError):
            account.withdraw(20000, 2222)

    def test_that_negative_amount_can_not_be_withdrawn(self):
        account = Account('chichi', '3506856011', '2222')
        with self.assertRaises(InvalidAmountError):
            account.withdraw(-1000, 2222)

    def test_that_amount_can_be_checked(self):
        account = Account('chichi', '3506856011', '2222')
        account.deposit(20000)
        self.assertEqual(20000, account.check_Balance('2222'))

    def test_for_wrong_pin_numbers(self):
        account = Account('chichi', '3506856011', '2222')
        account.deposit(2000)
        with self.assertRaises(InvalidPinError):
            account.check_Balance('2220')


