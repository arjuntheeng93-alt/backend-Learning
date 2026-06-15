import time
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.1f} seconds to execute.")
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Finished"

result = slow_function()
print(result)