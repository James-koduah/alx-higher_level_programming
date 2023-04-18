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
    results = session.query(State).filter(State.name == state_name) 
    try:
        print(results[0].name)
    except:
        print('Not found')
