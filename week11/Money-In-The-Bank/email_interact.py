import sqlite3
import smtplib
from password import generate_new_pass, hash_password
from queries import TAKE_EMAIL
from sql_manager import *

db = sqlite3.connect("bank.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


def generate_TAN_code(user):
    tan_list = []
    for _ in range(10):
        tan_list.append(generate_new_pass(size=32))
    msg = "Your TAN codes are:\n"

    if user.set_tan_codes(tan_list):
        send_mail(user.get_email(), msg)


def send_mail(reciever, msg):
    print(reciever)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("ivanmilevtues@gmail.com", "------")
    server.sendmail("ivanmilevtues@gmail.com", reciever, msg)
    server.quit()


def reset_password():
    user = input("Username:$$$>")
    emails = cursor.execute(TAKE_EMAIL, [user, ])
    email = ''
    for e in emails:
        email = e['email']

    new_pass = generate_new_pass()
    msg = "Your new password is {0}".format(new_pass)

    new_pass = hash_password(new_pass)
    change_pass(new_pass, user)

    send_mail(email, msg)

if __name__ == '__main__':
    send_mail()
