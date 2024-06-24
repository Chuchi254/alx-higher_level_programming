#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_04_usa.
The script takes 3 arguments: mysql username, mysql password,
and database name.
It connects to a MySQL server running on localhost at port 3306
and retrieves all cities sorted by cities.id in ascending order.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL  database
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
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cur.execute(query)

    # Fetch all the rows in the result set
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
