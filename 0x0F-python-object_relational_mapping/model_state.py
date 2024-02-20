#!/usr/bin/python3
"""
Author: Mire-web
Desc: Definition of State an dInstance of base
Date: 20/02/2024
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
