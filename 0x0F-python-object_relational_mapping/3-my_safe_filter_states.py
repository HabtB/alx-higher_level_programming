#!/usr/bin/python3
"""
This script takes arguments and displays all values in the states table of
`hbtn_0e_0_usa` where name matches the argument. In addition, it considers
SQL injection and uses parameterized queries. """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database_name> <state_name>"
              .format(sys.argv[0]))
        exit(1)

    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    state_name = argv[4]
    db_cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    params = (state_name,)

    db_cursor.execute(query, params)

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
