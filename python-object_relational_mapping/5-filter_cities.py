#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Open database
    db = MySQLdb.connect("localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT cities.name FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   WHERE states.name = %s\
                   ORDER BY cities.id ASC", (state_name, ))

    # Print results
    cities_list = [row[0] for row in cursor.fetchall()]

    print(", ".join(cities_list))

    # Close cursors
    cursor.close()
    # Close connection to the database
    db.close()
