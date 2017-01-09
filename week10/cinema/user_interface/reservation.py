# TODO
# Make the printing matrix and you will be ok!
# Update Querry too.
from queries.manage_db_queries import SELECT_RESERVATIONS, INSERT_RESERVATION, DELETE_RESERVATION
from settings.general_settings import DB_NAME, SharedVariables
from movie import *
from datetime import datetime
from validators import *
import sqlite3

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

ROWS = 10
COLS = 10

FREE = 'O'
TAKEN = 'X'


def log_info(func, *args, **kwargs):
    def decorated(wanted_tickets, projection_id, *args, **kwargs):
        with open("/home/imilev/workspace/hackbulgaria/python_101/python101/week10/cinema/database/log.txt", "a") as f:
            f.write("{0} User with id: {1} reserved {2} tickets.\n".format(
                    str(datetime.now()), SharedVariables.user_id,
                    len(wanted_tickets)))
        return func(wanted_tickets, projection_id, *args, **kwargs)
    return decorated


def check_free_tickets(wanted_tickets, projection_id):
    reservations = c.execute(SELECT_RESERVATIONS, [projection_id, ])
    if ROWS * COLS - sum(1 for reservation in reservations) < wanted_tickets:
        print("Not enough free positions!")
        return False
    return True


def pprint(matrix):
    row_num = 1
    print('   ', end="")
    for a in range(1, COLS+1):
        print(a, end=" ")
    for row in matrix:
        print()
        if(row_num < 10):
            print(str(row_num), end="  ")
        else:
            print(str(row_num), end=" ")
        for el in row:
            print(el, end=" ")
        row_num += 1
    print()


def print_free_spots(projection_id):
    spots = [[FREE for x in range(COLS)] for x in range(ROWS)]
    reservations = c.execute(SELECT_RESERVATIONS, [projection_id, ])
    taken_spots = []
    for reservation in reservations:
        spots[reservation['ROW']][reservation['COL']] = TAKEN
        taken_spots.append((reservation['ROW'], reservation['COL']))
    pprint(spots)
    return set(taken_spots)


@log_info
def finalize(reserv_positions, projection_id):
    for spot in reserv_positions:
        c.execute(INSERT_RESERVATION, [spot[0], spot[1],
                                       SharedVariables.user_id,
                                       projection_id, ])
    db.commit()
    print("Your reservation has been made successfully!")
    print("Have a great time watching the movie!")


@user_exists
def make_reservation():
    tickets = int(input("How many tickets do you want to buy: "))
    show_movies()
    movie_id = input("Select movie by id: ")
    show_projections([movie_id])
    projection_id = input("Select projection by id: ")

    if check_free_tickets(tickets, projection_id):
        print("Please choose spots")
        taken = print_free_spots(projection_id)

        i = 0
        reserv_tickets = []
        while i < tickets:
            row = int(input("Your row:"))
            col = int(input("Your column:"))

            if (row, col) not in taken and validate_row_col(row, col):
                i += 1
                reserv_tickets.append((row, col))
                taken.add((row, col))
            else:
                print("Spot already taken.\nChoose new one.")

        confirm = input("finalize or give up:")
        if confirm == "finalize":
            finalize(reserv_tickets, projection_id)
        elif confirm == "give up":
            print("You gave up your reservation.")
        else:
            print("Wrong input!")
    else:
        print("Not enough free tickets for the chosen projection.")


@user_exists
def cancel_reservation(name):
    str_name = ''
    if type(name) is list:
        for word in name:
            str_name = str_name + ' ' + word
        str_name = str_name[1:]
    else:
        str_name = name
    print(str_name)
    if str_name != SharedVariables.username:
        print("You don't have the permistion to do that!")
    else:
        c.execute(DELETE_RESERVATION, [SharedVariables.user_id, ])
        db.commit()
        print("Your reservation was canceled.")
