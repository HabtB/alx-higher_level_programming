#!/usr/bin/python3
"""
This script defines a City class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sys import argv


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
