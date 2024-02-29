from ac.BankApplication.Account import Account
from ac.BankApplication.InsufficientFundError import InsufficientFundError


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.__generate = 0

    def registerCustomer(self, first_name, last_name, pin):
        full_name = f"{first_name} {last_name}"
        account = Account(full_name, self.__generateAccount(), pin)
        self.accounts.append(account)  # Append the Account object
        return account

    def __generateAccount(self):
        self.__generate = self.__generate + 1
        return self.__generate

    def findAccount(self, acct_number) -> Account:
        for account in self.accounts:
            if account.get_account_number() == acct_number:
                return account

    def get_number_of_Accounts(self):
        return len(self.accounts)

    def deposit(self, amount, acct_number):
        account = self.findAccount(acct_number)
        account.deposit(amount)

    def checkBalance(self, acct_number, pin):
        account = self.findAccount(acct_number)
        return account.check_Balance(pin)

    def withdraw(self, amount, acct_number, pin):
        account = self.findAccount(acct_number)
        account.withdraw(amount,pin)

    def transfer(self, senderAccountNumber, receiverAccountNumber, amount, pin):
        sender_account = self.findAccount(senderAccountNumber)
        receiver_account = self.findAccount(receiverAccountNumber)
        sender_account.withdraw(amount, pin)
        receiver_account.deposit(amount)






