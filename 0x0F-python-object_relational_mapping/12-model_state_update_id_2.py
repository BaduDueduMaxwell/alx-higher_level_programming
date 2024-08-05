#!/usr/bin/python3
"""
This script changes the name of a State object from the database `hbtn_0e_6_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql username> \
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
        state = session.query(State).filter(State.id == 2).first()

        if state:
            state.name = "New Mexico"
            session.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
