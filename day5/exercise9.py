#here i am making authentication decorator
is_logged_in = False
import functools
def required_login(func): #this is a decorator function that takes another function as an argument
    @functools.wraps(func) #this is a decorator that preserves the original function's metadata, such as its name and docstring, when it is decorated
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            return{"error": "unauthorized", "status": 401}

    return wrapper

@required_login
def dashboard():
    return "welcome to dashboard"

print(dashboard())

  

    