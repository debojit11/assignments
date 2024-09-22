'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests


url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(url)
data = response.json()
users = data['data']
emails = [user['email'] for user in users]
print("list of emails:")
print(emails)
