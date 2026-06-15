#Excepted output:
#calling and with args=(3,4) kwargs={}
#Calling greet eith args = () kwargs={'name': 'Arrow'}

import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b    

@log_calls
def greet(name):
    return f"Hello, {name}!"
print(add(3, 4))
print(greet("Arrow"))