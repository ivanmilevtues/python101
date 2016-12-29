import sqlite3
import getpass
import re
import sys

from settings import *
from queries import *
from password import *
from user import Patient
from doctor import Doctor

LOGGEDIN = 1
LOGOUT = 0

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def start_options():
    options = """
Welcome to Hospital Manager!
Main page:
Choose:
1 to Log into the system
2 to register as a new user
3 for help main
4 to exit the system. """
    print(options)
    return True



def login(*args):
    valid_username = False
    valid_pass = False
    user = None
    username = input("Username: ")
    password = getpass.getpass()
    users = c.execute(SELECT_USERS)
    password = encode_password(password)
    for user in users:
        if user['USERNAME'] == username:
            valid_username = True

            if user['PASSWORD'] == password:
                valid_pass = True
                print(user['USERNAME'], user['id'])
                c.execute(UPDATE_ACTIVE, (LOGGEDIN, user['id'], ))
                db.commit()
                if 'Dr.' in username:
                    user = Doctor(username, user['id'])
                else:
                    user = Patient(username, user['id'])

    if not valid_pass:
        if not valid_username:
            print("No user with this username!")
        else:
            print("Wrong password!")
    
    return user

def logout(user):
    c.execute(UPDATE_ACTIVE, [LOGOUT, user.get_id(), ])
    db.commit()
    start_options()
    return False


def register(*args):
    print(
        """
Password requirements:
At least one uppercase letter.
At least one lowercase letter.
At least one digit.
Length greater then 7.
""")
    username = input("Username: ")
    password = getpass.getpass()
    age = input("Age: ")
    if(validate_password(password)):
        c.execute(INSERT_INTO_USER, [username, encode_password(password),
                                     age, ])
        print("Registered successfuly!")
    else:
        print("Invalid password!")
    db.commit()
    return True


def exit(*args):
    users = c.execute(SELECT_USERS)
    for user in users:
        if user['IS_ACTIVE']:
            c.execute(UPDATE_ACTIVE, (LOGOUT, user['id'], ))
            print("Successfuly log out")
    db.commit()
    sys.exit()
    return False
