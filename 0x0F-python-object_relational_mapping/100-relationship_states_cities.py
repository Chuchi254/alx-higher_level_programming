#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco" in
the database hbtn_0e_100_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
It connects to a MySQL server running on localhost at port 3306 and adds the
State "California" with the City "San Francisco".
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

    # Create a Session()
    session = Session()

    # Create a new State object with a City
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add the new State (with the City) object to the session
    session.add(new_state)
    session.add(new_city)
    session.commit()

    # Print the new state's id and the new city's id
    print(f"State id: {new_state.id}")
    print(f"City id: {new_city.id}")

    # Close the session
    session.close()
