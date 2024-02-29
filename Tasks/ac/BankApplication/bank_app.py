from ac.BankApplication.Bank import Bank


class BankApp:
    def __init__(self):
        self.bank = Bank("Chichi bank")

    def main_menu(self):
        menu = """
        1. Create a bank account
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Find Account Number
        6. Transfer
        7. Exit"""

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
                BankApp.exit()

    def create_account(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        pin_number = input("Enter your pin number: ")

        account = self.bank.registerCustomer(first_name, last_name, pin_number)
        print("account number:", account.get_account_number())
        self.main_menu()

    def deposit(self):
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter amount to deposit: "))
        self.bank.deposit(amount, account_number)
        self.main_menu()

    def withdraw(self):
        account_number = int(input("Enter your account number: "))
        amount = int(input("Enter amount you want to withdraw: "))
        pin_number = input("Enter your pin number: ")
        self.bank.withdraw(amount, account_number, pin_number)
        self.main_menu()

    def checkBalance(self):
        account_number = int(input("Enter your account number: "))
        pin_number = input("Enter your pin number: ")
        result = self.bank.checkBalance(account_number, pin_number)
        print(result)
        self.main_menu()

    def findAccount(self):
        account_number = int(input("Enter your account number: "))
        account = self.bank.findAccount(int(account_number))
        print(account)
        self.main_menu()

    def transfer(self):
        senderAccountNumber = int(input("Enter your account number: "))
        receiverAccountNumber = int(input("Enter your receiver account number: "))
        amount = int(input("Enter the amount to transfer: "))
        pin_number = input("Enter your pin number: ")
        self.bank.transfer(senderAccountNumber, receiverAccountNumber, amount, pin_number)
        self.main_menu()

    @classmethod
    def exit(cls):
        pass


if __name__ == '__main__':
    app = BankApp()
    app.main_menu()
