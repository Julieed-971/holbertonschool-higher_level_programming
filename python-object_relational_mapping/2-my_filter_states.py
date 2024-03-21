#!/usr/bin/python3
"""List all values in states where name matches the argument"""

import sys
import MySQLdb


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_srch = sys.argv[4]

# Open database
    db = MySQLdb.connect("localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states WHERE states.name\
                   LIKE BINARY '{}' ORDER BY states.id ASC"
                   .format(state_name_srch))

    # Print results in tuple format
    for row in cursor.fetchall():
        print(row)

    # Close cursors
    cursor.close()

    # Close connection to the database
    db.close()
