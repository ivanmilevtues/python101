from sqlalchemy import Column, Integer, String, Float, ColumnDefault
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String)
    balance = Column(Float)
    message = Column(String)
    login_attempts = Column(Integer, ColumnDefault(0))
    timeot = Column(Integer, ColumnDefault(0))
