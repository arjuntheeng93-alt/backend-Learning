#count functtion calls
import functools

def count_calls(func):
    count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} called {count} times")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def hello():
    print("hello()")
    
hello()
hello()