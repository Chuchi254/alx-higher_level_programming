#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
It connects to a MySQL server running on localhost at port 3306 and
retrieves all City objects sorted in ascending order by cities.id.
The results are displayed as <city id>: <city name> -> <state name>.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine and connect to the MySQL database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
            )

    # Create all tables in the database (if not already created)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects and their corresponding State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
