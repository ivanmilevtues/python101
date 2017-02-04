from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column


Base = declarative_base()


class BaseUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable = False)
    last_name = Column(String(250), nullable = False)
    passworf = Column(String(250), nullable = False)
