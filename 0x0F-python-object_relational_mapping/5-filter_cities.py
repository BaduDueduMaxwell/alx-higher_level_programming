#!/usr/bin/python3
"""
This script lists all cities of states from the database `hbtn_0e_4_usa`
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
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    db_cursor.execute(query, (argv[4],))

    results = db_cursor.fetchall()

    city_names = ", ".join([result[0] for result in results])
    print(city_names)

    db_cursor.close()
    db_connect.close()
