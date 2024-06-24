#!/usr/bin/python3
"""
This script takes in the name of a state as argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
This script takes 4 arguments: mysql, mysql password,
database name, and state name.
It connects to a MySQL server running on localhost at port 3306
and retrieves all cities sorted by cities.id in ascendigng order.
This version is safe SQL Injection.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # Create the SQL query using a parameterized query to prevent SQL Injection
    query = (
            "SELECT cities.name "
            "FROM cities JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC"
            )
    cur.execute(query, (state_name,))

    # Fetch all the rows in the result set
    rows = cur.fetchall()

    # Print the rows as a comma-separated list
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Close the cursor and database connection
    cur.close()
    db.close()
