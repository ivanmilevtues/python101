# Refactored

from sqlalchemy import create_engine
from base import Base

engine = create_engine("sqlite:///Bank.db")

Base.metadata.create_all(engine)
