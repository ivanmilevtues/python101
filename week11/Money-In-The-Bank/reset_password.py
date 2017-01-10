import sqlite3
import smtplib
import string
import random
from password import generate_new_pass
from queries import TAKE_EMAIL

db = sqlite3.connect("bank.db")
db.row_factory = sqlite3.Row
cursor = db.cursor()


def send_mail(reciever):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("ivanmilevtues@gmail.com", "-----")

	msg = "Your password is {0}".format(generate_new_pass())

	server.sendmail("ivanmilevtues@gmail.com", reciever, msg)
	server.quit()


def reset_password()
	user = input("Username:$$$>")
	email = cursor.execute(TAKE_EMAIL)
	send_mail(email)

if __name__ == '__main__':
	send_mail()