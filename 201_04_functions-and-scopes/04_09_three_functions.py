# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def get_user_name():
    """
    Asks the user for their name and returns it.

    Returns:
        str: The name provided by the user.
    """
    name = input("What is your name? ")
    return name

def greet_user(name):
    """
    Greets the user by name and returns a greeting message.

    Args:
        name (str): The name of the user.

    Returns:
        str: A personalized greeting message.
    """
    greeting = f"Hello, {name}! Nice to meet you."
    return greeting

def print_greeting():
    """
    Gets the user's name, greets them, and prints the greeting.

    This function orchestrates the process by calling `get_user_name` 
    to retrieve the user's name, `greet_user` to create a greeting 
    message, and then prints the greeting message.
    """
    name = get_user_name()
    greeting = greet_user(name)
    print(greeting)

print_greeting()
