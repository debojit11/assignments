# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(offensive):
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


offensive= ["fuck","shit","hell", "damn"]
@censor(offensive)

def print_text(text):
    return text

print_text("Damn! I lost. How the hell did I lose?")