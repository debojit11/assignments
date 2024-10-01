# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time

def decorator_func(initial_func):
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        result = initial_func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {initial_func.__name__} executed in {execution_time:.50f} seconds")
        return result
    return wrapper_func


@decorator_func
def add(a,b):
    return a+b


@decorator_func
def my_function():
    time.sleep(2)

my_function()
print(add(3,5))