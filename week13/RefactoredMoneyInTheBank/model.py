# Refactored

from sqlalchemy import Column, Integer, String, Real
from base import Base


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    email = Column(String, nullable=True)
    balance = Column(Real)
    message = Column(String)
    login_attempts = Column(Integer, default=0)
    timeout = Column(Real, default=0)
    tan_codes = Column(String)
