#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
The script takes 4 arguments: mysql username, mysql passsword, database name,
and state name searched.
It connects to a MySQL server running on localhost at port 3306
and retrieves all matching states sorted by dtates.id in ascending order.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line argments
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

    # Execute SQL query using a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the rows in the result set
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
