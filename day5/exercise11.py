import functools

def rate_limit(func):
    count = 0
    @functools.wraps(func)
    
    def wrapper(*args, **kwargs):
        
        nonlocal count
        count += 1
        if count > 3:
            return {"error": "Rate limit exceeded", "status": 428}
            
        return func (*args, **kwargs)
    return wrapper
@rate_limit
def get_user():
    return{"message": "user data", "status": 200}
    
get_user()
get_user()
get_user()
get_user()
get_user()
get_user()