from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Movies, Projections, Users, Reservations
from start import Base

engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def main():
    print("Filling the database with information...")
    # Adding users
    session.add_all([
        Users(username="Pesho", password="123456"),
        Users(username="Mitko", password="123456"),
        Users(username="Totko", password="123456"),
        Users(username="Vanka", password="123456")])
    session.commit()

    session.add_all([
        Movies(name="The Hunger Games: Catching Fire", rating=7.9),
        Movies(name="Wreck-It Ralph", rating=7.8),
        Movies(name="Her", rating=8.3)])
    session.commit()

    session.add_all([
        Projections(movie_id=1, type="3D", date="2014-04-01", time="19:10"),
        Projections(movie_id=1, type="2D", date="2014-04-01", time="19:00"),
        Projections(movie_id=1, type="4DX", date="2014-04-02", time="21:00"),
        Projections(movie_id=3, type="3D", date="2014-04-05", time="20:20"),
        Projections(movie_id=2, type="3D", date="2014-04-02", time="22:00"),
        Projections(movie_id=2, type="2D", date="2014-04-02", time="19:30")])
    session.commit()

    session.add_all([
        Reservations(user_id=3, projection_id=1, row=2, col=1),
        Reservations(user_id=3, projection_id=1, row=3, col=5),
        Reservations(user_id=3, projection_id=1, row=7, col=8),
        Reservations(user_id=2, projection_id=3, row=1, col=1),
        Reservations(user_id=2, projection_id=3, row=1, col=2),
        Reservations(user_id=5, projection_id=5, row=2, col=3),
        Reservations(user_id=6, projection_id=5, row=2, col=4)])
    session.commit()

    print("Database generated")


if __name__ == '__main__':
    main()
