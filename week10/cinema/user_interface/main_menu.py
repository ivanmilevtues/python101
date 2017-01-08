import sqlite3
import re
from interface import *
from validators import args_validate
from settings.general_settings import *
from queries.manage_db_queries import *

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def parse_input(user_input):
    args = user_input.split(' ')
    func_args = []
    if "show movie projection" in user_input:
        func_args.append(args[0] + ' ' + args[1] + ' ' + args[2])
        start_point = 3
    else:
        func_args.append(args[0] + ' ' + args[1])
        start_point = 2

    for indx in range(start_point, len(args)):
        func_args.append(args[indx])

    return func_args


def show_movies():
    movies = c.execute(SELECT_MOVIES)
    print("Movie:")
    for movie in movies:
        print("[{0}] - {1} ({2})".format(movie['ID'], movie['NAME'],
                                         movie['RATING']))


@args_validate
def show_projections(*args):
    pass


def print_main():
    print(MAIN_MENU)


def logout():
    pass


def close_program():
    logout()
    exit()


FUNC_DICT = {
    "show movie projection": show_projections,
    "show movies": show_movies,
    "help": print_main,
    "exit": close_program
}


def call_function(func_args):
    if type(func_args) is list:
        if func_args[0] in FUNC_DICT.keys():
            FUNC_DICT[func_args[0]](func_args[1:])
        else:
            print("Wrong input!")
    else:
        if func_args in FUNC_DICT.keys():
            FUNC_DICT[func_args]()
        else:
            print("Wrong input!")


def main():
    print_main()
    while(1):
        user_input = input('> ')
        if len(user_input.split(' ')) > 2:
            call_function(parse_input(user_input))
        else:
            call_function(user_input)


if __name__ == '__main__':
    main()
