import sqlite3
from settings.sql_creation import DB_NAME
from queries.create_db_queries import *

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()
db.commit()


def create_database():
    c.execute(CREATE_MOVIE_TABLE)
    c.execute(CREATE_USER_TABLE)
    c.execute(CREATE_PROJECTION_TABLE)
    c.execute(CREATE_RESERVATION_TABLE)
    db.commit()

def drop_tables():
    c.execute(DROP_MOVIE_TABLE)
    c.execute(DROP_PROJECTION_TABLE)
    c.execute(DROP_USER_TABLE)
    c.execute(DROP_RESETVATION_TABLE)


def insert_movies():
    users = [("The Hunger Games: Catching Fire", 7.9),
             ("Wreck-It Ralph", 7.8),
             ("Her", 8.3)]
    c.executemany(INSERT_MOVIE, users)


def insert_projections():
    projections = [(1, "3D", "2014-04-01", "19:10"),
                   (1, "2D", "2014-04-01", "19:00"),
                   (1, "4DX", "2014-04-02", "21:00"),
                   (3, "2D", "2014-04-05", "20:20"),
                   (2, "3D", "2014-04-02", "22:00"),
                   (2, "2D", "2014-04-02", "19:30")]
    c.executemany(INSERT_PROJECTION, projections)


def insert_reservations():
    reservations = [(3, 1, 2, 2),
                    (3, 1, 3, 5),
                    (3, 1, 7, 8),
                    (2, 3, 1, 1),
                    (2, 3, 1, 2),
                    (5, 5, 2, 3),
                    (6, 5, 2, 4)]
    c.executemany(INSERT_RESERVATION, reservations)


def insert_users():
    users = [("Rositsa Zlateva", "1234567"),
             ("Slavayana Monkova", "1234567890"),
             ("Radoslav Georgiev", "1234567890"),
             ("Krasimira Badova", "1234567890"),
             ("Kiril Hristov", "1234567890"),
             ("Vladimir Delchev", "1234567890")]
    c.executemany(INSERT_USER, users)


def main():
    drop_tables()
    create_database()
    insert_movies()
    insert_projections()
    insert_reservations()
    insert_users()
    db.commit()
    db.close()

if __name__ == '__main__':
    main()
