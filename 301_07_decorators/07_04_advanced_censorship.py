# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor(*offensive):
    def decorator_func(initial_func):
        def wrapper_func(*args):
            result = initial_func(*args)
            for word in offensive:
                censor_word = word[0] + "*" * (len(word)-1)
                result = result.replace(word, censor_word)
                result = result.replace(word.capitalize(), censor_word.capitalize())
            print(result)
        return wrapper_func
    return decorator_func



@censor("hell","damn","shit")

def print_text(text):
    return text

print_text("Damn! I lost. How the hell did I lose?")