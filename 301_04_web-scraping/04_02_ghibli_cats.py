# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.



import requests

BASE_URL = "https://ghibliapi.dev"

# Get the species classified as "cat"
response = requests.get(f"{BASE_URL}/species?name=cat")
species_data = response.json()

print("Studio Ghibli Cats:")

# Check if species data is returned
if species_data:
    for species in species_data:
        if species['name'].lower() == 'cat':
            for person_url in species['people']:
                person_uuid = person_url.split("/")[-1]  # Extract UUID from URL
                person_response = requests.get(f"{BASE_URL}/people/{person_uuid}")
                person_data = person_response.json()

                # Print cat details
                data_name = person_data['name']
                data_gender = person_data['gender']
                data_age = person_data.get('age', 'Unknown')  # Default to 'Unknown'
                data_hair_color = person_data.get('hair_color', 'Unknown')
                data_eye_color = person_data.get('eye_color', 'Unknown')

                print(f"name: {data_name}, gender: {data_gender}, age: {data_age}, "
                      f"hair color: {data_hair_color}, eye color: {data_eye_color}")
else:
    print("No species found.")
