# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.


import requests

# Define the base URLs for the APIs
ghibli_url = "https://ghibliapi.dev"
poke_url = "https://pokeapi.co/api/v2/type/ghost"

# Get the species that are classified as "Spirit" from the Ghibli API
ghibli_response = requests.get(f"{ghibli_url}/species?name=spirit")
ghibli_species = ghibli_response.json()
# print(ghibli_species)
ghibli_ghosts = []
if ghibli_species:
    for species in ghibli_species:
        # Filter based on classification as "Spirit"
        if species['name'].lower() == 'spirit':
            for person_url in species['people']:
                person_uuid = person_url.split("/")[-1]  # Extract UUID from URL
                person_response = requests.get(f"https://ghibliapi.dev/people/{person_uuid}")
                person_data = person_response.json()
                ghibli_ghosts.append(person_data['name'])

# Get Ghost-type Pokémon from the PokeAPI
poke_response = requests.get(poke_url)
poke_data = poke_response.json()

# Extract Pokémon names
poke_ghosts = [pokemon_data['pokemon']['name'] for pokemon_data in poke_data['pokemon']]

# Print all Ghibli Spirits first
print("Ghibli Spirits:")
for ghost in ghibli_ghosts:
    print(f"- {ghost}")

# Print all Ghost Pokémon next
print("\nGhost Pokémon:")
for poke_ghost in poke_ghosts:
    print(f"- {poke_ghost}")

