#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database `hbtn_0e_6_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql username> \
<mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
@localhost:3306/{dbname}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    try:
        new_state = State(name="Louisiana")

        session.add(new_state)

        session.commit()

        print(new_state.id)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
