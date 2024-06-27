from pydantic import BaseModel
# Import the 'BaseModel' class from Pydantic. This class is used to define data validation and serialization models.

class BookCreate(BaseModel):
    # Define a class 'BookCreate' that inherits from 'BaseModel'. This class represents the schema for creating a book.

    title: str
    # Define an attribute 'title' with type 'str'. This attribute is required when creating a book.

    price: str
    # Define an attribute 'price' with type 'str'. This attribute is required when creating a book.

    availability: str
    # Define an attribute 'availability' with type 'str'. This attribute is required when creating a book.

    class Config:
        orm_mode = True
        # Define a nested 'Config' class to provide configurations for the Pydantic model.
        # 'orm_mode = True' configures the Pydantic model to work with ORMs (Object-Relational Mappers) like SQLAlchemy.
        # This allows Pydantic to read data from SQLAlchemy models and return data that can be converted to JSON.
