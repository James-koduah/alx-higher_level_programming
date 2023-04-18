#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'state'

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(128))

