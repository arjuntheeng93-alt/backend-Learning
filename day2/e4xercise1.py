def show_args(*args):
    for item in args:
        print(item)
        
def show_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        
show_args(1,2,3, "hello") 
show_kwargs(name="Arjun", age=22, country = "Nepal")
