#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`
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

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    db_cursor.execute(query)

    results = db_cursor.fetchall()

    for result in results:
        print(result)

    db_cursor.close()
    db_cursor.close()
