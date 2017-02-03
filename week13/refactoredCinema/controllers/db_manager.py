from prettytable import PrettyTable
from models.tables import Movies, Projections, Users, Reservations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.start import Base

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
    filter_args = args[0]
    table = PrettyTable(['ID', 'Movie ID', 'Type', 'Date', 'Time'])
    if len(filter_args) == 2:
        projections = session.query(Projections).\
            filter(Projections.movie_id == filter_args[0],
                   Projections.date == filter_args[1])
    else:
        projections = session.query(Projections).\
            filter(Projections.movie_id == filter_args[0])
    for p in projections:
        table.add_row([p.id, p.movie_id, p.type, p.date, p.time])
    print(table)
