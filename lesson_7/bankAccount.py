class BankAccount:

    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError
        self.name = name
        self.balance = balance
        self.currency = currency
        self.history = ["Account was created"]

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount
        self.history.append("Deposited {0}{1}".format(amount, self.currency))

    def get_balance(self):
        self.history.append("Balance check --> {0}{1}".format(self.balance,
                                                              self.currency))
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance = self.balance - amount

    def __str__(self):
        return "BankAccount for {0} with balance of {1}{2}".format(self.name,
                                                                   self.balance,
                                                                   self.currency)

    def __int__(self):
        self.history.append("__int__ check -> {0}{1}".format(self.balance,
                                                             self.currency))
        return self.balance

    def transfer_to(self, account, amount):
        if amount > self.balance:
            self.history.append("withdraw for {0}{1} failed".format(amount,
                                                                    self.currency))
            return False
        elif account.currency != self.currency:
            self.history.append("withdraw for {0}{1} failed".format(amount,
                                                                    self.currency))
            return False
        else:
            self.history.append("withdraw for {0}{1}".format(amount,
                                                             self.currency))
            account.balance += amount
            self.balance -= amount
            return True

    def get_history(self):
        return self.history


def main():
    account = BankAccount("Rado", 0, "$")
    print(account)
    print(account.deposit(1000))
    print(account.get_balance())
    print(str(account))
    print(int(account))
    print(account.get_history())
    print(account.withdraw(500))
    print(account.get_balance())
    print(account.get_history())
    print(account.withdraw(1000))
    print(account.get_balance())
    print(account.get_history())

if __name__ == "__main__":
    main()
