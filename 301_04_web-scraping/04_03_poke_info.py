# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5



import requests
import json

# Base URL for the Pokémon API
BASE_URL = "https://pokeapi.co/api/v2/"

# List of your favorite Pokémon (use their names or IDs)
favorite_pokemons = ['pikachu', 'charizard', 'bulbasaur', 'eevee', 'gengar', 'snorlax']

# Initialize an empty list to hold Pokémon data
pokemon_data = []

# Fetch data for each Pokémon
for pokemon in favorite_pokemons:
    response = requests.get(BASE_URL + f"pokemon/{pokemon}")  # Correctly specify the Pokémon name in the URL
    data = response.json()  # Directly parse the JSON response
    pokemon_info = {
        'name': data['name'],
        'number': data['id'],
        'types': [type_info['type']['name'] for type_info in data['types']],
        'sprite': data['sprites']['front_default']  # Get the default sprite
    }
    pokemon_data.append(pokemon_info)

# Print the fetched Pokémon data
print(json.dumps(pokemon_data, indent=2))
