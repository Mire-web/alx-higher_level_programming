#!/usr/bin/python3
"""
Author: Mire-web
Desc: Lists all state object from database
Date: 20/02/2024
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


args = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_list = session.query(State).order_by(State.id.asc()).all()
    for state in state_list:
        print(state.id, ': ', state.name)
