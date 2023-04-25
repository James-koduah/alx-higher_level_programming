#!/usr/bin/python3
'''
    Lists all state names in a database
'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    n, username, passwd, db_name = sys.argv
    engine = create_engine(
            f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db_name}"
            )
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(bind=engine)
    lou = State()
    lou.name = "Louisiana"
    session.add(lou)
    session.commit()
    results = session.query(State).all()
    print(lou.id)
