#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa` with a name starting with N (upper N)
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%'")

    states = db_cursor.fetchall()

    for state in states:
        print(state)
