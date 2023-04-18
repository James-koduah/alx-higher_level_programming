#!/usr/bin/python3

'''
Fetch the first item of a table (states)
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    n, username, passwd, db_name = sys.argv
    engine = create_engine(
            f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db_name}"
            )
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(bind=engine)
    results = session.query(State).first()
    if results:
        print(f"1: {results.name}")
    else:
        print("Nothing")
