'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"
body = {
    "first_name": "Who",
    "last_name": "Cares",
    "email": "careswho@careswho.co"
}
response = requests.put(url + "/6925", json = body)
print(response.status_code)
responses = requests.get(url)
print(f"Content: {responses.content}")