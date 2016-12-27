import sqlite3
from settings import *
import getpass
from queries import *
from doctor import Doctor

LOGGEDIN = 1
LOGGEDOUT = 0

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def login():
	valid_username = False
	valid_pass = False

	username = input("Username: ")
	password = getpass.getpass()
	users = c.execute(SELECT_USERS)

	for user in users:
		if user['USERNAME'] == username:
			valid_username = True

			if user['PASSWORD'] == password:
				valid_pass = True
				c.execute(UPDATE_ACTIVE, (LOGGEDIN, user['id'], ))

				if 'Dr.' in username:
					Doctor(username, user['id'])
	if not valid_pass:
		if not valid_username:
			print("No user with this username!")
		else:
			print("Wrong password!")

	db.commit()
	return True


def register():
	pass

def exit():
	users = c.execute(SELECT_USERS)
	for user in users:
		if user['IS_ACTIVE']:
			c.execute(UPDATE_ACTIVE, (LOGGEDOUT, user['id'], ))
			print("Successfuly log out")
	db.commit()
	return False


def user_options():
	options = """
Welcome to Hospital Manager!
Choose:
1 to Log into the system
2 to register as a new user
3 for help main
4 to exit the system. """
	return options


CALL_FUNCTION = {
	1: login,
	2: register,
	3: user_options,
	4: exit
}


def control_block():
	print(user_options())
	while True:
		asked_func = ' '
		while asked_func not in ['1', '2', '3', '4'] :
			asked_func = input()
			print("Wrong input")

		if not CALL_FUNCTION[int(asked_func)]():
			break

def main():
	control_block()

if __name__ == '__main__':
	main()
