#!/usr/bin/python3
"""
This script lists all states objects from the database `hbtn_0e_6_usa`
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{database}')

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
