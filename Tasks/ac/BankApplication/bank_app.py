from ac.BankApplication.Bank import Bank
from ac.BankApplication.InsufficientFundError import InsufficientFundError
from ac.BankApplication.InvalidAccountNumber import InvalidAccountNumber
from ac.BankApplication.InvalidAmountError import InvalidAmountError
from ac.BankApplication.InvalidPinError import InvalidPinError


class BankApp:
    def __init__(self):
        self.bank = Bank("Chichi bank")

    def main_menu(self):
        menu = """
        1. Create a brb ank account
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Find Account Number
        6. Transfer
        7. Remove Account
        8. Exit"""

        print(menu)
        choice = input("Select an option: ")

        match choice:
            case "1":
                self.create_account()
            case "2":
                self.deposit()
            case "3":
                self.withdraw()
            case "4":
                self.checkBalance()
            case "5":
                self.findAccount()
            case "6":
                self.transfer()
            case "7":
                self.remove_account()
            case "8":
                BankApp.exit()

    def create_account(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        pin_number = input("Enter your pin number: ")

        try:
            account = self.bank.registerCustomer(first_name, last_name, pin_number)
            print("account number:", account.get_account_number())
            print("successfully registered")
        except Exception as e:
            print(e)

        self.main_menu()

    def deposit(self):
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter amount to deposit: "))
        try:
            account = self.bank.deposit(amount, account_number)
            print("successfully deposited")
        except InvalidAmountError as e:
            print(e)

        self.main_menu()

    def withdraw(self):
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter amount you want to withdraw: "))
        pin_number = input("Enter your pin number: ")

        try:
            bank = self.bank.withdraw(amount, account_number, pin_number)
            print("withdraw successfully ")
        except InvalidAmountError as e:
            print(e)
        self.main_menu()

    def checkBalance(self):
        account_number = int(input("Enter your account number: "))
        pin_number = input("Enter your pin number: ")
        try:
            result = self.bank.checkBalance(account_number, pin_number)
            print(result)
        except InvalidPinError as e:
            print(e)
        self.main_menu()

    def findAccount(self):
        account_number = int(input("Enter your account number: "))
        try:
            account = self.bank.findAccount(account_number)
            if account_number == account:
                print(account)
            if account_number != account:
                print("account number found")
        except Exception as e:
            print(e)
        self.main_menu()

    def transfer(self):
        senderAccountNumber = int(input("Enter your account number: "))
        receiverAccountNumber = int(input("Enter your receiver account number: "))
        amount = int(input("Enter the amount to transfer: "))
        pin_number = input("Enter your pin number: ")

        try:
            self.bank.transfer(senderAccountNumber, receiverAccountNumber, amount, pin_number)
            print("Transfer successful")
        except InsufficientFundError as e:
            print(e)
        except InvalidAmountError as e:
            print(e)

        self.main_menu()

    def remove_account(self):
        account_number = int(input("Enter your account number: "))
        pin_number = input("Enter your pin number: ")

        try:

            account = self.bank.remove_account(account_number, pin_number)
            print("Account removed successfully")
        except BaseException as e:
            print(e)

        self.main_menu()

    @classmethod
    def exit(cls):
        pass


if __name__ == '__main__':
    app = BankApp()
    app.main_menu()
