from ac.BankApplication.Account import Account
from ac.BankApplication.InsufficientFundError import InsufficientFundError
from ac.BankApplication.InvalidAccountNumber import InvalidAccountNumber


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.number = 0
        #self.number_of_account = 0

    def registerCustomer(self, first_name, last_name, pin):
        Account.validate(pin)
        full_name = f"{first_name} {last_name}"
        account_number = self.__generateAccountNumber()
        account = Account(full_name, account_number, pin)
        self.accounts.append(account)  # Append the Account object
        return account

    def __generateAccountNumber(self):
        self.number += 1
        return self.number

    def findAccount(self, acct_number):
        expected_account = None
        for account in self.accounts:
            if account.get_account_number() == acct_number:
                expected_account =  account
        if expected_account is None:
            raise InvalidAccountNumber("account not found")
        return expected_account
    def get_number_of_Accounts(self):
        return self.number

    def deposit(self, amount, acct_number):
        account = self.findAccount(acct_number)
        account.deposit(amount)

    def checkBalance(self, acct_number, acctPin):
        account = self.findAccount(acct_number)
        return account.check_Balance(acctPin)

    def withdraw(self, amount, acct_number, pin):
        account = self.findAccount(acct_number)
        account.withdraw(amount, pin)

    def transfer(self, senderAccountNumber, receiverAccountNumber, amount, pin):
        sender_account = self.findAccount(senderAccountNumber)
        receiver_account = self.findAccount(receiverAccountNumber)
        sender_account.withdraw(amount, pin)
        receiver_account.deposit(amount)

    def remove_account(self, acct_number, pin):
        for account in self.accounts:
            account = self.findAccount(acct_number)
            if account.get_account_number() == acct_number:
                self.accounts.remove(account)
