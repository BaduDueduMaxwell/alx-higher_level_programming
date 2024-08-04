#!/usr/bin/python3
"""
This script defines a State class and creates an instance of declarative_base
to link the State class to a MySQL table
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base and links to the MySQL table status.
    Attributes:
        id (int): Uniquere integer, auto-generated, primary key, can't be null.
        name (str): String with a maximum of 128 characters, can't be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    if __name__ == "__main__":
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], \
                sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
