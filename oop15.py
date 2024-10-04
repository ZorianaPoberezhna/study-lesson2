class Account:
    def __init__(self, account_holder, balance=0):
        self.__balance = balance
        self._account_holder = account_holder

    @property
    def account_balance(self):
        return self.__balance

    @account_balance.setter
    def account_balance(self, value):
        if value > 0:
            self.__balance = value
        else:
            raise ValueError ("Error: the balance must be greater than zero ")

account = Account("John Bee", 1000)
account.account_balance = 500
