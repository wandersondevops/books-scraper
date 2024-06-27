from sqlalchemy.orm import Session
# Import the Session class from SQLAlchemy's ORM. This will be used to interact with the database session.

from . import models, schemas
# Import models and schemas from the current package. 'models' contains the database models, and 'schemas' contains the Pydantic schemas.

def create_book(db: Session, book: schemas.BookCreate):
    # Define a function 'create_book' that takes a database session 'db' and a book schema 'book' as parameters.
    
    db_book = models.Book(title=book.title, price=book.price, availability=book.availability)
    # Create an instance of the Book model with the title, price, and availability fields from the book schema.

    db.add(db_book)
    # Add the new book instance to the current database session.

    db.commit()
    # Commit the current transaction to the database, saving the new book instance.

    db.refresh(db_book)
    # Refresh the instance to get any updated fields from the database (like the id).

    return db_book
    # Return the newly created book instance.
