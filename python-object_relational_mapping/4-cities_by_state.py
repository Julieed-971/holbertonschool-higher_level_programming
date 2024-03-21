#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Open database
    db = MySQLdb.connect("localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")

    # Print results in tuple format
    for row in cursor.fetchall():
        print(row)

    # Close cursors
    cursor.close()
    # Close connection to the database
    db.close()
