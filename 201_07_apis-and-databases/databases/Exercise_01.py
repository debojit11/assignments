'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
from sqlalchemy import create_engine, MetaData, Table

# Replace these with your actual database credentials
DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/sakila"

# Create an engine to connect to the Sakila database
engine = create_engine(DATABASE_URL)

# Create a MetaData instance
metadata = MetaData()

# Reflect the existing tables
metadata.reflect(bind=engine)

# Access the 'film' and 'category' tables
film_table = Table('film', metadata, autoload_with=engine)
category_table = Table('category', metadata, autoload_with=engine)

# Print table information
print("Film Table Columns:")
for column in film_table.columns:
    print(column.name, column.type)

print("\nCategory Table Columns:")
for column in category_table.columns:
    print(column.name, column.type)
