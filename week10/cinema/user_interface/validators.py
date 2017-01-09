import re
from logger import *
from settings.general_settings import SharedVariables


def user_exists(func, *args, **kwargs):
    def exists(*args, **kwargs):
        print(SharedVariables.sessiong_log)
        if SharedVariables.sessiong_log:
            return func(*args, **kwargs)
        else:
            print("""You are not logged into the system.
Would you please login:""")
            return log_in()
    return exists


def validate_row_col(row, col):
    if row > 0 and row <= 10 and col > 0 and col <= 10:
        return True
    else:
        return False


def validate_passw(func, *args, **kwargs):
    def validator(passw, *args, **kwargs):
        if len(passw) < 8:
            print("Password too short")
            return False
        if not re.search(r"\d", passw):
            print("No digits in the password!")
            return False
        if not re.search(r"[a-z][A-Z]", passw):
            print("Upper or lower case letters missing!")
            return False
        return func(passw)
    return validator

# def args_validate(*args):
#     print("Someone here")
#
#     def get_func(func):
#         def checker(*args):
#             print(type(args), ' -> ', args)
#             if type(args) is list:
#                 if len(args) > 2:
#                     print("Too much arguments given!")
#                     return False
#                 for indx in range(len(args)):
#                     if indx == 0:
#                         if not re.match(r"\d+", args[indx]):
#                             print("First argument has wrong format!")
#                             return False
#                     if indx == 1:
#                         if not re.match(r"\[\d+-\d+-\d+\]+", args[indx]):
#                             print("Second argument has wrong format!")
#                             return False
#             return func()
#     return get_func
