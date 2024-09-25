class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance


    def withdraw(self, amount):
        if amount > self.balance:
            print("There are not enough funds in the account.")
        else:
            self.balance -= amount


    def topup(self, amount):
        self.balance += amount


    def __str__(self):
        return f"You account balance is:{self.balance}"

account = BankAccount(100)
account.withdraw(50)
account.topup(200)
print(account)

