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
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    state_name = argv[4]
    db_cursor = db.cursor()
    db_cursor.execute("SELECT cities.name FROM cities\
                       JOIN states ON cities.state_id = states.id\
                       where states.name = %s", (state_name,))

    city = [row[0] for row in db_cursor.fetchall()]

    print((", ") .join(city))
