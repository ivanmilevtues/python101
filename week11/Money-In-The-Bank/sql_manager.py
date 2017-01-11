import time
import sqlite3
from client import Client
from queries import *

db = sqlite3.connect("bank.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


FIVE_MINS = 300


def update_balance(balance, user):
    cursor.execute(UPDATE_BALANCE, [balance, user, ])
    db.commit()


def create_clients_table():
    # cursor.execute(DROP_DB)
    cursor.execute(CREATE_QUERY)
    print("Datebase has been created!")


def change_message(new_message, logged_user):
    cursor.execute(UPDATE_SQL, [new_message, logged_user, ])
    db.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute(UPDATE_SQL, [new_pass, logged_user, ])
    db.commit()


def register(username, password, email):
    cursor.execute(INSERT_USER, [username, password, email, ])
    db.commit()


def login(username, password):
    attempts = 0
    users = cursor.execute(SELECT_USER, [username, ])
    login_res = False

    for usr in users:
        if int(usr['login_attempts']) > 5 and username == usr['username']:
            cursor.execute(BAN_FOR_5min, [time.time() + FIVE_MINS, username, ])
        elif username == usr['username']:
            attempts = usr['login_attempts'] + 1
            print(password, usr['password'])
            if password == usr['password']:
                login_res = True
                user = usr

    if(login_res):
        cursor.execute(UPDATE_ATTEMPTS, [username, attempts, ])
        db.commit()
        return Client(user['id'], user['username'], user['balance'],
                      user['message'], user['email'])
    else:
        cursor.execute(UPDATE_ATTEMPTS, [username, attempts + 1, ])
        db.commit()
        return False

if __name__ == "__main__":
    create_clients_table()
