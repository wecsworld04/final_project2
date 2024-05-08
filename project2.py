class Account:
    def __init__(self, name, balance=0):
        self.__account_name = name
        self.__account_balance = balance
        self.set_balance(balance)

    def deposit(self, amount):
        if amount >= 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

    def set_balance(self, value):
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value

    def set_name(self, value):
        self.__account_name = value

    def __str__(self):
        return f"Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}"


class SavingAccount(Account):
    minimum = 100
    rate = 0.02

    def __init__(self, name):
        super().__init__(name, self.minimum)
        self.__deposit_count = 0

    def apply_interest(self):
        if self.__deposit_count % 5 == 0 and self.__deposit_count != 0:
            rate = self.get_balance() * self.rate
            self.deposit(rate)

    def deposit(self, amount):
        if amount <= 0:
            return False
        else:
            deposited = super().deposit(amount)
            if deposited:
                self.__deposit_count += 1
                self.apply_interest()
                return deposited

    def withdraw(self, amount):
        if amount <= 0 or amount > self.get_balance() - self.minimum:
            return False
        result = super().withdraw(amount)
        return result

    def set_balance(self, value):
        if value < self.minimum:
            self.__account_balance = self.minimum
        else:
            super().set_balance(value)

    def __str__(self):
        return f"SAVING ACCOUNT: {super().__str__()}"
