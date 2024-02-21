#!/usr/bin/python3
"""
Author: Mire-web
Desc: Lists all city object from database
Date: 21/02/2024
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


args = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State).order_by(City.id).all()
    print(cities)
    for state in cities:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")
