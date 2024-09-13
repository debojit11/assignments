# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, text):
    """Write a letter with a greeting, a message, and a goodbye."""
    greeting = f"Dear {name},\n"
    goodbye = f"\nBest regards,\n{name}"
    letter = greeting + text + goodbye
    return letter


print(write_letter("debojit", "this is a function"))