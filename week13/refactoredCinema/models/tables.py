from sqlalchemy import Column, Integer, String, Float, ForeignKey
from start import Base


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Float)


class Projections(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movies.id))
    type = Column(String, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Users.id))
    projection_id = Column(Integer, ForeignKey(Projections.id))
    row = Column(Integer)
    col = Column(Integer)
