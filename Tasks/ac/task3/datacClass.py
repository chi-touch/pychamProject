from dataclasses import dataclass
@dataclass(order =True)
class Account:
    name :str
    balance :Decimal

    def withdraw(self, amount:Decimal):
        return self.balance - amount
