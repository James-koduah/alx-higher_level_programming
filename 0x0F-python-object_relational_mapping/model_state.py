#!/usr/bin/python3
"""
My first class model of sqlalchemy
"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    """A state model"""
    __tablename__ = 'states'

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128))
