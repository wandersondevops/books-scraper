from sqlalchemy import Column, Integer, String
# Import the 'Column', 'Integer', and 'String' classes from SQLAlchemy.
# 'Column' is used to define columns in the database table.
# 'Integer' and 'String' specify the data types for the columns.

from .database import Base
# Import the 'Base' class from the 'database' module. This is the base class for all the models.

class Book(Base):
    # Define a class 'Book' that inherits from 'Base'. This class represents the 'books' table in the database.

    __tablename__ = 'books'
    # Specify the name of the database table as 'books'.

    id = Column(Integer, primary_key=True, index=True)
    # Define an 'id' column with the 'Integer' type. This column is the primary key of the table and is indexed for faster lookups.

    title = Column(String, index=True)
    # Define a 'title' column with the 'String' type. This column is indexed to allow faster searches by title.

    price = Column(String)
    # Define a 'price' column with the 'String' type.

    availability = Column(String)
    # Define an 'availability' column with the 'String' type.
