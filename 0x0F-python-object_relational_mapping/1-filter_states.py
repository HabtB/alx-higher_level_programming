#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from
database `hbtn_0e_0_usa`.
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

    db_cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%'"

    db_cursor.execute(query)

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
