# Add type annotations to the three functions shown below.

def multiply(num1, num2):
    """
    Multiplies two numbers and returns the result.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of multiplying num1 and num2.
    """
    return num1 * num2

def greet(greeting, name):
    """
    Creates a greeting message.

    Args:
        greeting (str): The greeting message.
        name (str): The name of the person.

    Returns:
        str: A greeting message.
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args):
    """
    Prints each item in the shopping list and returns the list of items.

    Args:
        *args (str): The items in the shopping list.

    Returns:
        tuple[str, ...]: A tuple of items in the shopping list.
    """
    [print(f"* {item}") for item in args]
    return args