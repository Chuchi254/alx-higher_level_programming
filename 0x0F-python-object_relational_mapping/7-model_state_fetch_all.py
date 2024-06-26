#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
The script takes 3 argument: mysql username, mysql password,
it connects to a MySQL server running on localhost at port 3306
all State objects sorted by states.id in ascending order.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Bind the engine to the Base's metadata
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session()
    session = Session()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
