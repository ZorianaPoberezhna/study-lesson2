from  abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_info(self):
        pass

class Customer(Person):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.__customer_id = customer_id

    def get_info(self):
        return {f"Name: {self._name}"
                f"Email: {self._email}"
                f"Customer ID: {self.__customer_id}"}

    @property
    def customer_id(self):
        return self.__customer_id

class BankAccount:
    def __init__(self, balance, owner, account_number):
        self.__balance = balance
        self._owner = owner
        self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            raise ValueError ("The balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} has been added to the account. Current balance: {self.__balance}")
        else:
            raise ValueError ("The top-up amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= 0:
                self.__balance -= amount
                print(f"{amount} has been withdrawn from the account. Current balance: {self.__balance}")
            else:
                raise ValueError ("There are insufficient funds in the account")
        else:
            raise ValueError ("The withdrawal amount must be greater than 0")

    def get_account_number(self):
        return self.__account_number

customer = Customer("Kevin Raw", "kewin.raw@example.com", customer_id=1234)
bank_account = BankAccount(owner=customer, account_number="UA1234567890", balance=1000)
print(customer.get_info())

bank_account.deposit(500)
bank_account.withdraw(200)
print(bank_account.get_account_number())