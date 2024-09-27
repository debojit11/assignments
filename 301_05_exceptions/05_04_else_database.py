# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import mysql.connector
from mysql.connector import Error

# Database connection parameters
host = 'localhost'  # Change if your server is different
database = 'your_database_name'  # Replace with your database name
user = 'your_username'  # Replace with your MySQL username
password = 'your_password'  # Replace with your MySQL password

try:
    # Attempt to establish a connection to the database
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

except Error as e:
    # Handle the error if the connection fails
    print(f"Error: {e}")

else:
    # This block executes if the try block succeeds
    if connection.is_connected():
        print("Successfully connected to the database!")
        # You can perform database operations here
        connection.close()  # Close the connection when done
    else:
        print("Failed to connect to the database.")