#!/usr/bin/python3

'''
List state objects that contain the letter 'a'
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    n, username, passwd, db_name, state_name = sys.argv
    engine = create_engine(
            f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db_name}"
            )
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(bind=engine)
    results = session.query(State)
    not_exists = 1
    for state in results:
        if state.name == state_name:
            print(state.id)
            not_exists = 0
            break;

    if not_exists:
        print('Not found')
