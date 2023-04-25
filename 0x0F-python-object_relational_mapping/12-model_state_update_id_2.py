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
    results = session.query(State)
    for row in results:
        if row.id == 2:
            row.name = 'New Mexico'
            session.add(row)
            session.commit()
