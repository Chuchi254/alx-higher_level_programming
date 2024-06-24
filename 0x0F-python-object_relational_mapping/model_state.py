#!/usr/bin/python3
"""
This module defines a State class and an instance of declarative_base().
"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    State class that represents a table in a MySQL database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    if __name__ == "__main__":
        import sys
        # Get MySQL credentials from command line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Create an enigne and connect to the MySQL database
        engine = create_engine(
                f'mysql+mysqldb://{username}:{password}@localhost:3306/'
                f'{database}',
                pool_pre_ping=True
                )

        # Create all tables in the database
        Base.metadata.create_all(engine)
