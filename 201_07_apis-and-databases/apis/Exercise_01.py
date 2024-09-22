'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body



'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(url)
print(f"Status Code: {response.status_code}")
print(f"Encoding :{response.encoding}")
pprint(f"Text of body :{response.text}")
