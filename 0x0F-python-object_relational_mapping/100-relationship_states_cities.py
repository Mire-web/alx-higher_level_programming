#!/usr/bin/python3
"""
Author: Mire-web
Desc: Create State and cities in database
Date: 22/02/2024
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
import sys


args = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    new_city = City(name="San Francisco")
    new_state = State(name="California")
    new_city.state = new_state
    add_all = [new_state, new_city]
    session.add_all(add_all)
    session.commit()
    session.close()
