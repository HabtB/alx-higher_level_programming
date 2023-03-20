#!/usr/bin/python3
""" """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)
session = Session()

first_state = session.query(State).order_by(State.id).first()
if first_state:
    print("{}: {}".format(first_state.id, first_state.name))
else:
    print('Nothing')
