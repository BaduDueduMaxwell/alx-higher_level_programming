#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
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

    query = "SELECT * FROM states WHERE BINARY name = '{}'".format(argv[4])
    db_cursor.execute(query)

    states = db_cursor.fetchall()

    for state in states:
        print(state)
