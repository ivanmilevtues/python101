class Client():
    def __init__(self, id, username, balance, message, email):
        self.__username = username
        self.__balance = int(balance)
        self.__id = id
        self.__message = message
        self.__email = email
        self.__tan_codes = []

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def get_email(self):
        return self.__email

    def set_message(self, new_message):
        self.__message = new_message

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_tan_codes(self):
        return self.__tan_codes

    def set_tan_codes(self, new_tan_codes):
        if len(self.__tan_codes):
            print("Sorry you have {0} TAN codes left".format(
                len(self.__tan_codes)))
            return False
        else:
            self.__tan_codes = new_tan_codes
            print("Check you email for the new TAN codes!")
            return True
