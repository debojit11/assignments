'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"
body= {
    "first_name": "Who",
    "last_name": "Cares",
    "email": "whocares@careswho.co"
}
response = requests.post(url, json = body)
print(response.status_code)