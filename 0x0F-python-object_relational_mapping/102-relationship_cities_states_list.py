#!/usr/bin/python3
"""
Author: Mire-web
Desc: List all city objects from database
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State.name).\
        join(State, State.id == City.state_id).\
        order_by(City.id.asc()).all()
    for city, state_name in cities:
        print(f"{city.id}: {city.name} -> {state_name}")
