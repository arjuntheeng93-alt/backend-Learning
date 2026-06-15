import functools

def my_decorator(func): #this is a decorator function that takes another function as an argument
    @functools.wraps(func) #this is a decorator that preserves the original function's metadata, such as its name and docstring, when it is decorated
    def wrapper(*args, **kwargs): #this is the wrapper function that will be returned by the decorator, it will call the original function and add some additional behavior, it takes any number of positional and keyword arguments and passes them to the original function
        print(f"Calling {func.__name__}") #this will be printed before the original function is called, it uses the __name__ attribute of the original function to print its name
        result = func(*args, **kwargs) #call the original function with the arguments passed to the wrapper function and store the result in the variable result
        print(f"Finished {func.__name__}")
        return result #return the result of the original function
        
    return wrapper #return the wrapper function

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name):
    return f"Hello, {name}!"

print(add(3,4))
print(greet("puppy"))