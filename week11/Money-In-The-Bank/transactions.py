from sql_manager import update_balance


class Transaction:
    def __init__(self, user):
        self.__user = user

    def TAN_code(self):
        tan = input("Enter TAN code:")
        tan_codes = self.__user.get_tan_codes()
        if tan in tan_codes:
            tan_codes.remove(tan)
            self.__user.set_tan_codes(tan_codes)
            return True
        else:
            print("Invalid TAN code. Check if you have any left!")
            return False

    def get_user(self):
        return self.__user

    def deposit(self, amount):
        if self.TAN_code():
            curr_balance = self.__user.get_balance()
            self.__user.set_balance(curr_balance + amount)
            update_balance(self.__user.get_balance(),
                           self.__user.get_username())

    def withdraw(self, amount):
        if self.TAN_code():
            curr_balance = self.__user.get_balance()
            if curr_balance < amount:
                print("You do not have enough money for this operation!")
                return False

            curr_balance -= amount
            self.__user.set_balance(curr_balance)
            update_balance(self.__user.get_balance(),
                           self.__user.get_username())

    def __str__(self):
        return "Client: {0} has {1}$ in his account.".format(
                                                self.__user.get_username(),
                                                self.__user.get_balance())

    def __repr__(self):
        return self.__str__()
