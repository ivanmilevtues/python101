import sql_manager
import getpass
from interface import *
from password import *

def register():
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ")
    
    if validate_password(password):
        password = hash_password(password)
        sql_manager.register(username, password)
        print("Registration Successfull")
    else:
        print("Password doesn't meet the needed requirements!")


def login():
    username = input("Enter your username: ")
    password = getpass.getpass(prompt="Enter your password: ")
    password = hash_password(password)

    logged_user = sql_manager.login(username, password)

    if logged_user:
        logged_menu(logged_user)
    else:
        print("Login failed")


def print_help():
    print(HELP_MSG)


def end_program(*args, **kvargs):
    exit()


CALL_MAIN_COMMANDS = {
    "register": register,
    "login": login,
    "help": print_help,
    "exit": end_program
}


def main_menu():
    print(WELCOME_MSG)

    while True:
        command = input("$$$>")

        if command not in CALL_MAIN_COMMANDS.keys():
            print("Not a valid command")
            continue         
        else:
            CALL_MAIN_COMMANDS[command]()


def show_info(logged_user):
    print("You are: " + logged_user.get_username())
    print("Your id is: " + str(logged_user.get_id()))
    print("Your balance is:" + str(logged_user.get_balance()) + '$')


def changepass(logged_user):
    new_pass = getpass.getpass(prompt="Enter your new password: ")
    new_pass = hash_password(new_pass)
    sql_manager.change_pass(new_pass, logged_user)


def change_message(logged_user):
    new_message = input("Enter your new message: ")
    sql_manager.change_message(new_message, logged_user)


def show_message(logged_user):
    print(logged_user.get_message())


def show_help(*args, **kvargs):
    print(LOGGED_USER_HELP)


CALL_LOGGED_COMMANDS = {
    "info": show_info,
    "changepass": changepass,
    "change-message": change_message,
    "show-message": show_message,
    "help": show_help,
    "exit": end_program
}


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")
        if command not in CALL_LOGGED_COMMANDS.keys():
           print("Not a valid command")
        else:
            CALL_LOGGED_COMMANDS[command](logged_user)


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
