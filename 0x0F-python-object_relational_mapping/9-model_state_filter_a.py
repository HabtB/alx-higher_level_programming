#!/usr/bin/python3
""" 
This script lists all State objects
that contain the letter `a`
from the database `hbtn_0e_6_usa`.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
#    query = session.query(State).filter(State.name.contains('a'))
    for state in query.all():
        print("{}: {}".format(state.id, state.name))
