# this is normal decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
    return wrapper

# this is a decorator with arguments

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times = 3)
def greet():
    print("Hello!")    

greet()