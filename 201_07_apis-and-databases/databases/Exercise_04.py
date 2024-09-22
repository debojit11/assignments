'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!


'''

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, update, delete, select
from sqlalchemy.orm import sessionmaker
import argparse

# Database connection parameters
DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/my_database"

# Create the engine and metadata
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define tables
def create_tables():
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column('email', String)
                  )

    orders = Table('orders', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('user_id', Integer),
                   Column('product', String),
                   Column('amount', Integer)
                   )

    products = Table('products', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String),
                     Column('price', Integer)
                     )

    metadata.create_all(engine)
    print("Tables created successfully.")

# Insert data
def insert_data():
    users = Table('users', metadata, autoload_with=engine)
    orders = Table('orders', metadata, autoload_with=engine)
    products = Table('products', metadata, autoload_with=engine)

    with engine.connect() as conn:
        conn.execute(users.insert(), [
            {'name': 'Alice', 'email': 'alice@example.com'},
            {'name': 'Bob', 'email': 'bob@example.com'}
        ])
        conn.execute(products.insert(), [
            {'name': 'Laptop', 'price': 1200},
            {'name': 'Phone', 'price': 800}
        ])
        conn.execute(orders.insert(), [
            {'user_id': 1, 'product': 'Laptop', 'amount': 1},
            {'user_id': 2, 'product': 'Phone', 'amount': 2}
        ])
    print("Data inserted successfully.")

# Update data
def update_data():
    users = Table('users', metadata, autoload_with=engine)
    orders = Table('orders', metadata, autoload_with=engine)

    with engine.connect() as conn:
        conn.execute(update(users).where(users.c.name == 'Alice').values(email='alice@newdomain.com'))
        conn.execute(update(orders).where(orders.c.product == 'Phone').values(amount=3))
    print("Data updated successfully.")

# Select data
def select_data():
    users = Table('users', metadata, autoload_with=engine)
    orders = Table('orders', metadata, autoload_with=engine)
    products = Table('products', metadata, autoload_with=engine)

    with engine.connect() as conn:
        # Select all users
        result = conn.execute(select(users))
        print("\nUsers:")
        for row in result:
            print(row)

        # Select all orders and join with users
        query = select([orders, users]).select_from(orders.join(users, orders.c.user_id == users.c.id))
        result = conn.execute(query)
        print("\nOrders with user information:")
        for row in result:
            print(row)

        # Select all products
        result = conn.execute(select(products))
        print("\nProducts:")
        for row in result:
            print(row)

# Delete data
def delete_data():
    users = Table('users', metadata, autoload_with=engine)
    orders = Table('orders', metadata, autoload_with=engine)
    products = Table('products', metadata, autoload_with=engine)

    with engine.connect() as conn:
        conn.execute(delete(users).where(users.c.name == 'Bob'))
        conn.execute(delete(products).where(products.c.name == 'Phone'))
    print("Data deleted successfully.")

# CLI interface
def main():
    parser = argparse.ArgumentParser(description="Database Application CLI")
    parser.add_argument('--create', action='store_true', help='Create tables')
    parser.add_argument('--insert', action='store_true', help='Insert data')
    parser.add_argument('--update', action='store_true', help='Update data')
    parser.add_argument('--select', action='store_true', help='Select data')
    parser.add_argument('--delete', action='store_true', help='Delete data')
    
    args = parser.parse_args()

    if args.create:
        create_tables()
    if args.insert:
        insert_data()
    if args.update:
        update_data()
    if args.select:
        select_data()
    if args.delete:
        delete_data()

if __name__ == "__main__":
    main()
