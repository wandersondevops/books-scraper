from sqlalchemy import create_engine
# Import the 'create_engine' function from SQLAlchemy. This function is used to create a new SQLAlchemy engine instance.

from sqlalchemy.ext.declarative import declarative_base
# Import the 'declarative_base' function from SQLAlchemy. This function returns a base class for declarative class definitions.

from sqlalchemy.orm import sessionmaker
# Import the 'sessionmaker' function from SQLAlchemy. This function creates a configured "Session" class.

import os
# Import the 'os' module to interact with the operating system, particularly to get environment variables.

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
# Get the database URL from an environment variable named 'SQLALCHEMY_DATABASE_URL'.

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Create a new SQLAlchemy engine instance using the database URL. The engine represents the core interface to the database.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a configured "Session" class. Instances of this class will be used to interact with the database.
# - autocommit=False: Transactions are not automatically committed.
# - autoflush=False: Changes are not automatically flushed to the database.
# - bind=engine: The session will use the specified engine.

Base = declarative_base()
# Create a base class for declarative class definitions. This base class will be used to define the database models.

def init_db():
    Base.metadata.create_all(bind=engine)
    # Define a function 'init_db' that creates all tables in the database which are defined by subclasses of Base.
    # The 'metadata.create_all' method uses the engine to create the tables.
