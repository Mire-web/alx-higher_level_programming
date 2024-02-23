#!/usr/bin/python3
"""
Author: Mire-web
Desc: Lists all states and cities in database
Date: 23/02/2024
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


args = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    all_states = session.query(City).join(State).order_by(State.id.asc()).all()
    for state in all_states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
