# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(name):
    """Return a greeting string with the given name."""
    return f"Hello, {name}!"

def write_letter(name, text):
    """Write a letter with a greeting, a message, and a goodbye."""
    greeting = greet(name) + ",\n"
    goodbye = f"\nBest regards,\n{name}"
    letter = greeting + text + goodbye
    return letter


print(write_letter("debojit", "this is a function"))