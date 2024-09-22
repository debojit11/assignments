# Include the current weather into your game mechanics.


import random
import requests
import os  # Used to check if the file exists

URL = "https://www.metaweather.com/api/"

def save_game(player_name, inventory, doors_chosen, current_language, translation_history):
    """Saves the current game state to a file."""
    with open('game_save.txt', 'w') as file:
        file.write(f"{player_name}\n")
        file.write(",".join(inventory) + "\n")
        file.write(f"{doors_chosen['left']},{doors_chosen['right']}\n")
        file.write(f"{current_language}\n")
        file.write(f"{translation_history['from']},{translation_history['to']}\n")

def load_game():
    """Loads the game state from a file if it exists."""
    if not os.path.exists('game_save.txt'):
        return None, [], {"left": False, "right": False}, "en", {"from": "en", "to": "en"}

    with open('game_save.txt', 'r') as file:
        file_content = file.readlines()

    player_name = file_content[0].strip()
    inventory = file_content[1].strip().split(",") if file_content[1].strip() else []
    doors_status = file_content[2].strip().split(",")
    doors_chosen = {"left": doors_status[0] == "True", "right": doors_status[1] == "True"}
    current_language = file_content[3].strip()
    translation_history = dict(zip(["from", "to"], file_content[4].strip().split(",")))

    return player_name, inventory, doors_chosen, current_language, translation_history

def get_random_name(min_len=2, max_len=40):
    """Gets a random name from Uzby API."""
    url = f"https://uzby.com/api.php?min={min_len}&max={max_len}"
    response = requests.get(url)
    return response.text

def translate_text(text, source_lang, target_lang):
    """Translates text using LibreTranslate API."""
    url = "https://libretranslate.com/translate"
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang
    }
    response = requests.post(url, data=payload)
    return response.json()['translatedText']

def get_weather(location):
    """Fetches the current weather for a given location."""
    search_url = f"{URL}api/location/search/?query={location}"
    response = requests.get(search_url)
    if response.status_code == 200 and response.json():
        woeid = response.json()[0]['woeid']  # Get the WOEID for the location
        weather_url = f"{URL}api/location/{woeid}/"
        weather_response = requests.get(weather_url)
        return weather_response.json()['consolidated_weather'][0]['weather_state_name']
    return None

def choose_door(doors_chosen, inventory):
    """Handles the player's choice of doors and updates the game state accordingly."""
    available_doors = []
    if not doors_chosen["left"]:
        available_doors.append("left")
    if not doors_chosen["right"]:
        available_doors.append("right")
    
    print(f'{"You return to the two doors.":^30}')
    if available_doors:
        print(f'{"Available doors are: " + ", ".join(available_doors):^30}')
    
    choice = ""
    while choice not in available_doors:
        choice = input(f'{"Which door do you want to choose? (left/right): ":^30}').lower()

    if choice == "left" and not doors_chosen["left"]:
        print(f'{"You are in a room with no doors. It is empty.":^30}')
        if input(f'{"Do you want to look around? (yes/no): ":^30}').lower() == "yes":
            print(f'{"You see a sword on the ground.":^30}')
            if input(f'{"Do you want to take the sword? (yes/no): ":^30}').lower() == "yes":
                inventory.append("sword")
                print(f'{"You took the sword!":^30}')
            else:
                print(f'{"You left the sword.":^30}')
        doors_chosen["left"] = True

    elif choice == "right" and not doors_chosen["right"]:
        print(f'{"You enter a room and find a shield!":^30}')
        if input(f'{"Do you want to take the shield? (yes/no): ":^30}').lower() == "yes":
            inventory.append("shield")
            print(f'{"You took the shield!":^30}')
        else:
            print(f'{"You left the shield.":^30}')
        doors_chosen["right"] = True
    
    save_game(player_name, inventory, doors_chosen, current_language, translation_history)
    return doors_chosen, inventory

def combat(choice, inventory):
    """Handles combat encounters with enemies based on player's choices and items."""
    if choice == "dragon":
        print(f'{"You enter a room with a fierce dragon!":^30}')
        if input(f'{"Do you want to fight the dragon? (yes/no): ":^30}').lower() == "yes":
            if "sword" in inventory:
                print(f'{"Rolling the dice to see the outcome...":^30}')
                if random.randint(1, 6) > 3:
                    print(f'{"You defeated the dragon with your sword!":^30}')
                else:
                    if "shield" in inventory:
                        print(f'{"The dragon overpowered you, but your shield saved you!":^30}')
                        inventory.remove("shield")
                    else:
                        print(f'{"The dragon overpowered you and you lost the game!":^30}')
                        inventory.clear()
            else:
                print(f'{"You were eaten by the dragon because you had no sword!":^30}')
                inventory.clear()
    elif choice == "goblin":
        print(f'{"You enter a room with a sneaky goblin!":^30}')
        if input(f'{"Do you want to fight the goblin? (yes/no): ":^30}').lower() == "yes":
            if "sword" in inventory:
                print(f'{"Rolling the dice to see the outcome...":^30}')
                if random.randint(1, 6) > 2:
                    print(f'{"You defeated the goblin with your sword!":^30}')
                else:
                    if "shield" in inventory:
                        print(f'{"The goblin tricked you, but your shield protected you!":^30}')
                        inventory.remove("shield")
                    else:
                        print(f'{"The goblin tricked you and you lost the game!":^30}')
                        inventory.clear()
            elif "shield" in inventory:
                print(f'{"The goblin attacked, but your shield saved you!":^30}')
                inventory.remove("shield")
            else:
                print(f'{"The goblin defeated you because you had no sword or shield!":^30}')
                inventory.clear()
    return inventory

def play_game():
    """Main function that runs the game logic."""
    player_name, inventory, doors_chosen, current_language, translation_history = load_game()

    if not player_name:
        player_name = input(f"{'Enter Your Name: ':^30}")
        
        if 2 <= len(player_name) <= 40:
            in_game_name = get_random_name(len(player_name), len(player_name))
            print(f"{'Your in-game name is: ' + in_game_name:^30}")
        else:
            print(f"{'Your name must be between 2 and 40 characters.':^30}")
            return
    
    location = input("Enter your location (e.g., city name): ")
    weather = get_weather(location)
    
    if weather:
        print(f"The current weather in {location} is: {weather}")
        if "Rain" in weather:
            print(f'{"You found an umbrella!":^30}')
            inventory.append("umbrella")
        elif "Clear" in weather:
            print(f'{"You found a pair of sunglasses!":^30}')
            inventory.append("sunglasses")
        elif "Snow" in weather:
            print(f'{"You found a warm coat!":^30}')
            inventory.append("warm coat")
    
    language_switch = input(f"Do you want to switch to another language? (yes/no): ").lower()
    
    if language_switch == "yes":
        new_language = input(f"Enter the language code you'd like to switch to (e.g., 'fr' for French): ").lower()
        translated_welcome = translate_text("Welcome to the land of adventure!", current_language, new_language)
        print(f'{translated_welcome:^30}')
        current_language = new_language
        translation_history['to'] = current_language

    while not all(doors_chosen.values()):
        doors_chosen, inventory = choose_door(doors_chosen, inventory)
    
    print(f'{"You now see two more doors: one leads to a dragon, and the other to a goblin.":^30}')
    next_choice = input(f'{"Which door will you choose? (dragon/goblin): ":^30}').lower()
    inventory = combat(next_choice, inventory)
    
    if "sword" in inventory:
        print(f"Congratulations, {player_name}! You finished the game with a sword!")
    if "shield" in inventory:
        print(f"Congratulations, {player_name}! You finished the game with a shield!")
    if not inventory:
        print(f"Thank you for playing, {player_name}, but you lost all your items!")

    save_game(player_name, inventory, doors_chosen, current_language, translation_history)

# Start the game
play_game()
