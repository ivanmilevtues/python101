from queries.manage_db_queries import SELECT_USERS, UPDATE_ACTIVE
from settings.general_settings import DB_NAME, SharedVariables
import getpass
import sqlite3

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

LOGGEDIN = 1
LOGGEDOUT = 0


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
