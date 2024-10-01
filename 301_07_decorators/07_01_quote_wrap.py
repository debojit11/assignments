# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def decorator_func(initial_func):
    def wrapper_func(*args):
        result = initial_func(*args)
        return f'"{result}"'
    return wrapper_func 

@decorator_func
def print_text(text):
    return text

print(print_text("Hello World"))