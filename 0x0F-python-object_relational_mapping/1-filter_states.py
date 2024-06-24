#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
This script takes 3 arguments: mysql username, mysql password, and
database name.
It connects to a MySQL server running on localhost at port 3306
and retrieves all states sorted by states.id in ascending order
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MYSQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
            )

    # Fetch all the rows in the result set
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
