# Create a virtual environment and edit the activation script to add
# the following information:
# 
# - ENVIRONMENT="development"
# - SECRET="i ate your sweets"
# 
# Then write the necessary code to access and print the values of these
# two environment variables in this script.

import os

# Access environment variables with default values
environment = os.environ.get('ENVIRONMENT', 'Not Defined')
secret = os.environ.get('SECRET', 'Not Defined')

# Print the values
print(f'ENVIRONMENT: {environment}')
print(f'SECRET: {secret}')