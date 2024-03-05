import unittest

from ac.BankApplication.Bank import Bank
from ac.BankApplication.InsufficientFundError import InsufficientFundError
from ac.BankApplication.InvalidAccountNumber import InvalidAccountNumber


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bank = Bank('accessBank')

    def test_to_register_customer(self):
        self.bank.registerCustomer('chichi', 'ebu', '1234')
        self.assertEqual(1, self.bank.get_number_of_Accounts())

    def test_that_more_customer_can_added(self):
        self.bank.registerCustomer('chichi', 'alfred', '1234')
        self.bank.registerCustomer('mercy', 'moses', '4444')
        self.assertEqual(2, self.bank.get_number_of_Accounts())

    def test_that_i_can_find_account(self):
        account1 = self.bank.registerCustomer('chichi', 'alfred', '1234')
        account2 = self.bank.registerCustomer('mercy', 'moses', '4444')
        print(account1.get_account_number())
        self.bank.findAccount(account1)
        self.assertEqual(account1, self.bank.findAccount(1))

    def test_for_deposit(self):
        account = self.bank.registerCustomer('chichi', 'vic', '2222')
        self.bank.deposit(5000, 1)
        self.assertEqual(5000, self.bank.checkBalance(1, '2222'))

    def test_to_deposit_on_different_account(self):
        account1 = self.bank.registerCustomer('ayo', 'jojo', "1245")
        account2 = self.bank.registerCustomer('meshack', 'miriam', '3333')
        self.bank.deposit(2000, 2)
        print(self.bank.checkBalance(2, '3333'))
        self.assertEqual(2000, self.bank.checkBalance(2, '3333'))

    def test_for_withdraw(self):
        account1 = self.bank.registerCustomer('ayo', 'emeka', '5555')
        self.bank.deposit(4000, 1)
        self.bank.withdraw(3000, 1, "5555")
        self.assertEqual(1000, self.bank.checkBalance(1, '5555'))

    def test_that_amount_lesser_than_balance_can_not_be_withraw(self):
        account = self.bank.registerCustomer('ayo', 'evans', '3456')
        self.bank.deposit(3000, 1)
        self.assertRaises(InsufficientFundError, self.bank.withdraw, 5000, 1, '3456')

    def test_that_amount_can_be_transfered(self):
        self.bank.registerCustomer('ayo', 'orisha', "2345")
        self.bank.deposit(5000, 1)
        self.assertEqual(5000, self.bank.checkBalance(1, "2345"))

        self.bank.registerCustomer('hannah', 'josh', "4567")
        self.bank.transfer(1, 2, 3000, "2345")
        self.assertEqual(2000, self.bank.checkBalance(1, "2345"))
        self.assertEqual(3000, self.bank.checkBalance(2, "4567"))

    def test_that_account_can_be_removed(self):
        account1 = self.bank.registerCustomer('jack', 'mav', '4567')
        account2 = self.bank.registerCustomer('mesh', 'memiriam', '6789')

        self.bank.remove_account(2, '6789')
        # self.assertEqual("No Account found", self.bank.findAccount(account1.get_account_number()))
        self.assertEqual(2, self.bank.get_number_of_Accounts())

    def test_that_account_number__that_is_not_registered_cannot_removed(self):
        with self.assertRaises(InvalidAccountNumber):
            self.bank.findAccount(2)
