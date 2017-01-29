from prettytable import PrettyTable
from models.tables import Movies, Projections, Users, Reservations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from start import Base

engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def show_movies(*args, **kwargs):
    movies = session.query(Movies).all()
    table = PrettyTable(['ID', 'Name', 'Rating'])
    for movie in movies:
        table.add_row([movie.id, movie.name, movie.rating])
    print(table)


def show_movie_projection(*args, **kwargs):
    print(args)
