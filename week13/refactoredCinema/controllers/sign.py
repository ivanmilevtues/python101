from controllers.db_manager import check_for_user
from settings import SharedValues
from getpass import getpass


def log_in():
    username = input('> Username: ')
    password = getpass(prompt='> Password: ')
    user = check_for_user(username, password)
    if user:
        print('You have been logged successfuly!')
        SharedValues.user_logged = user
    else:
        print('No such user found!')


def log_out():
    SharedValues.user_logged = False
