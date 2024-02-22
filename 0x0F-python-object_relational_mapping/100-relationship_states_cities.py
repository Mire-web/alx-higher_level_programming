#!/usr/bin/python3
"""
Author: Mire-web
Desc: Create State and cities in database
Date: 22/02/2024
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
import sys


args = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = State()
    state.name = "California"
    city = City()
    city.name = "San Francisco"
    city.state_id = state.id
    add_all = [state, city]
    session.add_all(add_all)
    session.commit()
    session.close()
