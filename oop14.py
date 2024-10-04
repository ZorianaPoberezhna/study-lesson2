class Account:
    def __init__(self, account_holder, balance=0):
        self.__balance = balance
        self._account_holder = account_holder

    def __account_balance(self):
        return self.__balance

account = Account("John Bee", 1000)
