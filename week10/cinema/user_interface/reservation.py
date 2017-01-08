# TODO
# Make the printing matrix and you will be ok!
# Update Querry too.
from queries.manage_db_queries import SELECT_RESERVATIONS
from settings.general_settings import DB_NAME
import sqlite3

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()

ROWS = 10
COLS = 10


def check_free_tickets(wanted_tickets, projection_id):
    reservations = c.execute(SELECT_RESERVATIONS, [projection_id, ])
    if ROWS * COLS - sum(1 for reservation in reservations) < wanted_tickets:
        print("Not enough free positions!")
        return False
    return True


def print_free_spots(projection_id):
    reservations = c.execute(SELECT_RESERVATIONS, [projection_id, ])
    # for reservation in reservations:
