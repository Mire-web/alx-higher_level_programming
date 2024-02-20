#!/usr/bin/python3
"""
Author: Mire-web
Desc: Search and Print state from database
Date: 20/02/2024
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base,State
import sys


args = sys.argv
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb:{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == '{}'.\
                                         format(args[4])).first()
    if result:
        print(result.id)
    else:
        print("Not found")
