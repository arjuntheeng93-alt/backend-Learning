import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
        
    return wrapper

@my_decorator
def add(a, b):  
    return a + b

print(add.__name__)
print(add(3, 4))

#here i understand why i should use functools