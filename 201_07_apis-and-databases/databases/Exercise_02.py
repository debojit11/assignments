'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, select, and_, func

# Database connection parameters
DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/sakila"

# Create an engine to connect to the Sakila database
engine = create_engine(DATABASE_URL)

# Create a MetaData instance
metadata = MetaData()

# Reflect the existing tables
metadata.reflect(bind=engine)

# Access the necessary tables
actor_table = Table('actor', metadata, autoload_with=engine)
film_table = Table('film', metadata, autoload_with=engine)
category_table = Table('category', metadata, autoload_with=engine)
film_actor_table = Table('film_actor', metadata, autoload_with=engine)

# 1. Select all the actors with the first name of your choice
first_name = 'John'  # Replace with your choice
query_1 = select([actor_table]).where(actor_table.c.first_name == first_name)
print("Actors with the first name '{}':".format(first_name))
with engine.connect() as conn:
    result = conn.execute(query_1)
    for row in result:
        print(row)

print("\n" + "="*40 + "\n")

# 2. Select all the actors and the films they have been in
query_2 = select([actor_table.c.first_name, actor_table.c.last_name, film_table.c.title]).\
    select_from(actor_table.join(film_actor_table).join(film_table))
print("Actors and the films they have been in:")
with engine.connect() as conn:
    result = conn.execute(query_2)
    for row in result:
        print(row)

print("\n" + "="*40 + "\n")

# 3. Select all the actors that have appeared in a category of a comedy of your choice
comedy_category = 'Comedy'  # Replace with your choice
query_3 = select([actor_table.c.first_name, actor_table.c.last_name]).\
    select_from(actor_table.join(film_actor_table).join(film_table).join(category_table)).\
    where(category_table.c.name == comedy_category)
print("Actors who have appeared in '{}' category:".format(comedy_category))
with engine.connect() as conn:
    result = conn.execute(query_3)
    for row in result:
        print(row)

print("\n" + "="*40 + "\n")

# 4. Select all the comedic films and sort them by rental rate
query_4 = select([film_table]).\
    select_from(film_table.join(category_table)).\
    where(category_table.c.name == comedy_category).\
    order_by(film_table.c.rental_rate)
print("Comedic films sorted by rental rate:")
with engine.connect() as conn:
    result = conn.execute(query_4)
    for row in result:
        print(row)

print("\n" + "="*40 + "\n")

# 5. Add a GROUP BY statement to the query selecting actors by the number of films
query_5 = select([actor_table.c.first_name, actor_table.c.last_name, func.count(film_actor_table.c.film_id).label('film_count')]).\
    select_from(actor_table.join(film_actor_table)).\
    group_by(actor_table.c.first_name, actor_table.c.last_name)
print("Actors grouped by the number of films they have been in:")
with engine.connect() as conn:
    result = conn.execute(query_5)
    for row in result:
        print(row)

print("\n" + "="*40 + "\n")

# 6. Add an ORDER BY statement to the grouped actors query
query_6 = select([actor_table.c.first_name, actor_table.c.last_name, func.count(film_actor_table.c.film_id).label('film_count')]).\
    select_from(actor_table.join(film_actor_table)).\
    group_by(actor_table.c.first_name, actor_table.c.last_name).\
    order_by(func.count(film_actor_table.c.film_id).desc())  # Order by film count descending
print("Actors ordered by the number of films they have been in (descending):")
with engine.connect() as conn:
    result = conn.execute(query_6)
    for row in result:
        print(row)
