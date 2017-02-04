from queries.manage_db_queries import INSERT_USER, SELECT_USERS, UPDATE_ACTIVE
from settings.general_settings import DB_NAME, SharedVariables
from validators import *
import getpass
import sqlite3
import base64
import hashlib


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

LOGGEDIN = 1
LOGGEDOUT = 0


def hash_password(func):
    def hasher(passw, *args, **kwargs):
        t_sha = hashlib.sha512(passw.encode()).hexdigest()
        passw = base64.b64encode(t_sha.digest())
        return func(passw)
    return hasher


@hash_password
@validate_passw
def set_password(passw):
    return passw


def register():
    username = input("Pick username: ")
    password = getpass.getpass(prompt="Pick password: ")
    password = set_password(password)
    c.execute(INSERT_USER, [username, password, LOGGEDOUT])
    db.commit()
    print("Registered successfully!")
    print("Now you can log in.")


def log_in():
    username = input("> Username: ")
    password = getpass.getpass(prompt='> Password: ')
    users = c.execute(SELECT_USERS)
    print("Logging in...")
    for user in users:
        if user['USERNAME'] == username:
            if user['PASSWORD'] == password:
                c.execute(UPDATE_ACTIVE, [LOGGEDIN, username])
                db.commit()
                print("Successfully logged in the system!")
                SharedVariables.sessiong_log = True
                SharedVariables.user_id = user['ID']
                SharedVariables.username = user['USERNAME']
                print(SharedVariables.sessiong_log)
                return True
            else:
                print("Wrong password")

    print('No user with such username!')
    return False


def log_out():
    users = c.execute(SELECT_USERS)
    print("Log out...")
    for user in users:
        if user['ACTIVE'] == 1:
            c.execute(UPDATE_ACTIVE, [LOGGEDOUT, user['USERNAME'], ])
    print('Successfully logged out from the system!')
    db.commit()
