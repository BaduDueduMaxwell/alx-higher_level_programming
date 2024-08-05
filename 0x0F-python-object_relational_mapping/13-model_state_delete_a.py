#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a' \
from the database `hbtn_0e_6_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql username> \
<mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{dbname}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    session = Session()

    try:
        states_to_delete = session.query(State).\
            filter(State.name.ilike('%a%')).all()

        for state in states_to_delete:
            session.delete(state)

        session.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
