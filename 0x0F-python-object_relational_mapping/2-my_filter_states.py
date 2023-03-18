#!/usr/bin/python3
"""
This script takes arguments and displays all values in the states table of
`hbtn_0e_0_usa` where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    state_name = argv[4]
    db_cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}'".format(state_name)

    db_cursor.execute(query)

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
