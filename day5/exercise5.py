#building a decorator that retries a function up to 3 times if it raises an exception
import random
import functools

def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {i+1} failed with error: {e}")
        print("All attempts failed.")
    return wrapper
@retry
def unstable_function():
    if random.random() < 0.7: #70% chance to raise an exception
        raise ValueError("Something went wrong!")
    return "Success!"

result = unstable_function()
print(result)