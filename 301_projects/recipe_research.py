# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

class Ingredients:
    def __init__(self):
        self.items = []
    
    def add_ingredients(self, ingredients_str):
        # Split the input string by commas and strip any extra whitespace
        ingredients_list = [ingredient.strip() for ingredient in ingredients_str.split(',')]
        self.items.extend(ingredients_list)

    def create_search_url(self):
        # Base URL for searching recipes (example using Google search)
        base_url = "https://www.google.com/search?q="

        # Join the ingredients with a '+' to create a query string
        query = "+".join(self.items) + "+recipe"

        # Return the full URL
        return base_url + query


def main():
    ingredients = Ingredients()
    
    # Prompt the user to input ingredients in a single line, separated by commas
    ingredients_str = input("Enter ingredients separated by commas: ").strip()
    
    # Add the ingredients to the list
    if ingredients_str:
        ingredients.add_ingredients(ingredients_str)
    
    # Generate and print the search URL
    search_url = ingredients.create_search_url()
    print("\nSearch for recipes using the following URL:")
    print(search_url)


if __name__ == "__main__":
    main()