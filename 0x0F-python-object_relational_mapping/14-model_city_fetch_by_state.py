#!/usr/bin/python3
"""
This script prints all City objects from the database `hbtn_0e_14_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql username> \
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
        cities = session.query(City, State).join(State).order_by(City.id).all()

        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()
