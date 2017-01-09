from settings.general_settings import DB_NAME
from queries.manage_db_queries import *
import sqlite3

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def show_movies():
    movies = c.execute(SELECT_MOVIES)
    print("Movie:")
    for movie in movies:
        print("[{0}] - {1} ({2})".format(movie['ID'], movie['NAME'],
                                         movie['RATING']))


# @args_validate
def show_projections(*argv):
    args = argv[0]
    if len(args) > 1:
        projections = c.execute(SELECT_PROJECTIONS_FOR_DATE,
                                [args[0], args[1], ])
        print("Projections for: {0} on {1}".format(args[0], args[1]))
    else:
        projections = c.execute(SELECT_PROJECTIONS, [args[0], ])
        print("Projections for: {0}".format(args[0]))

    for projection in projections:
        print("[{0}] - {1} {2} ({3})".format(projection['ID'],
                                             projection['DATE_'],
                                             projection['TIME_'],
                                             projection['TYPE']))
