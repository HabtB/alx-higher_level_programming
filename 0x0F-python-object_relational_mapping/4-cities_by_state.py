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

    db_cursor = db.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name\
                       FROM cities\
                       JOIN states ON cities.state_id = states.id\
                       ORDER BY cities.id ASC")

    cities = db_cursor.fetchall()

    for city in cities:
        print(city)
