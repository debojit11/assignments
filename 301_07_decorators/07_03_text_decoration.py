# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(symbol):
    def decorator_func(initial_func):
        def wrapper_func(*args, **kwargs):
            result = initial_func(*args, **kwargs)
            border = symbol * (len(result) + 10)
            print(border)
            print(result)
            print(border)
            return result
        return wrapper_func
    return decorator_func

@decorate("*")
def greet():
    return "Hello"

greet()    