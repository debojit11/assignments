'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, update

# Database connection parameters
DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/sakila"

# Create an engine to connect to the Sakila database
engine = create_engine(DATABASE_URL)

# Create a MetaData instance
metadata = MetaData()

# Reflect the existing tables
metadata.reflect(bind=engine)

# Access the 'film' table
film_table = Table('film', metadata, autoload_with=engine)

# Define the update statement
stmt = update(film_table).\
    where(film_table.c.length > 150).\
    values(rental_duration=10)

# Execute the update statement
with engine.connect() as conn:
    result = conn.execute(stmt)
    print(f"Number of rows updated: {result.rowcount}")
