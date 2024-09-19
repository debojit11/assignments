'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import sessionmaker

# Database connection parameters
DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/my_database"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define tables
def create_tables():
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(255), unique=True)
                  )

    tasks = Table('tasks', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('title', String(255)),
                  Column('completed', Integer)  # Assuming completed is stored as an integer (0 or 1)
                  )

    metadata.create_all(engine)
    print("Tables created successfully.")

# Fetch data from API
def fetch_data():
    url = "http://demo.codingnomads.co:8080/tasks_api/users"
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    return response.json()

# Persist data to database
def persist_data(data):
    users = Table('users', metadata, autoload_with=engine)
    tasks = Table('tasks', metadata, autoload_with=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for user in data:
        user_id = user['id']
        user_name = user['name']

        # Check if user already exists
        existing_user_query = select([users.c.id]).where(users.c.id == user_id)
        existing_user = session.execute(existing_user_query).fetchone()

        if existing_user is None:
            # Insert new user
            session.execute(users.insert().values(id=user_id, name=user_name))
        
        # Insert tasks
        for task in user['tasks']:
            task_id = task['id']
            task_title = task['title']
            task_completed = task['completed']
            
            # Check if task already exists
            existing_task_query = select([tasks.c.id]).where(tasks.c.id == task_id)
            existing_task = session.execute(existing_task_query).fetchone()

            if existing_task is None:
                # Insert new task
                session.execute(tasks.insert().values(id=task_id, user_id=user_id, title=task_title, completed=task_completed))

    # Commit all changes
    session.commit()
    session.close()

    print("Data persisted successfully.")

def main():
    create_tables()
    data = fetch_data()
    persist_data(data)

if __name__ == "__main__":
    main()