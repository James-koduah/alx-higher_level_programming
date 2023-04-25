#!/usr/bin/python3

'''
    Lists all state names in a database
'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
import sys

if __name__ == "__main__":
    n, username, passwd, db_name = sys.argv
    engine = create_engine(
            f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db_name}"
            )
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(bind=engine)
    results = session.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id)

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")
