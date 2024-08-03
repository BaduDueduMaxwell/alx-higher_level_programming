#!/usr/bin/python3
"""
   This script lists all states from
   db 'hbtn_0e_0_usa'
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="127.0.0.1", port=3306, user=username, \
                         passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    state = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
