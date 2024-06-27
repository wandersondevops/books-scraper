import subprocess
# Import the 'subprocess' module to allow running subprocesses from the Python code.

from fastapi import FastAPI, Depends, HTTPException
# Import necessary components from FastAPI: 'FastAPI' to create the application instance, 'Depends' for dependency injection, and 'HTTPException' for error handling.

from fastapi.middleware.cors import CORSMiddleware
# Import 'CORSMiddleware' from FastAPI to handle Cross-Origin Resource Sharing (CORS).

from sqlalchemy.orm import Session
# Import the 'Session' class from SQLAlchemy's ORM to manage database sessions.

from typing import List
# Import 'List' from the typing module to define list types for type hints.

from . import crud, models, schemas, database
# Import 'crud', 'models', 'schemas', and 'database' modules from the current package. These contain the CRUD operations, database models, Pydantic schemas, and database setup respectively.

app = FastAPI()
# Create an instance of the FastAPI class, which represents the FastAPI application.

# Initialize the database
database.init_db()
# Call the 'init_db' function to initialize the database, creating all tables defined by the models.

# CORS settings
origins = [
    "http://localhost:3000",  # React app running on localhost:3000
    "http://localhost:8000",  # FastAPI app running on localhost:8000
]
# Define a list of allowed origins for CORS. These are the addresses from which requests to the FastAPI app are permitted.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Add CORS middleware to the FastAPI app with the specified settings:
# - allow_origins: the origins allowed to make requests.
# - allow_credentials: whether to allow credentials (cookies, authorization headers, etc.).
# - allow_methods: the HTTP methods allowed.
# - allow_headers: the HTTP headers allowed.

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Define a dependency function 'get_db' that provides a database session.
# The session is yielded to the endpoint, and then closed after the request is processed.

@app.post("/books/", response_model=schemas.BookCreate)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)
# Define a POST endpoint '/books/' to create a new book.
# The function takes a 'book' schema and a database session (provided by the 'get_db' dependency).
# The 'crud.create_book' function is called to create the book in the database, and the created book is returned.

@app.get("/books/", response_model=List[schemas.BookCreate])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books
# Define a GET endpoint '/books/' to read books from the database.
# The function takes optional 'skip' and 'limit' parameters for pagination and a database session (provided by the 'get_db' dependency).
# The books are queried from the database with the specified offset and limit, and the list of books is returned.

@app.post("/run-scraper/")
def run_scraper():
    try:
        command = ["python", "scraper.py"]
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return {"status": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.stderr.decode()}
# Define a POST endpoint '/run-scraper/' to run a scraper script.
# The function attempts to run the 'scraper.py' script using 'subprocess.run'.
# If successful, it returns a success status. If there is an error, it catches the exception and returns an error status with the stderr output.
