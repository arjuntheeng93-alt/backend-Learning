# today i am going to learn decorator 
def my_decorator(func): #this is a decorator function that takes another function as an argument
    def wrapper(): #this is the wrapper function that will be returned by the decorator, it will call the original function and add some additional behavior
        print("Before the function is called") #this will be printed before the original function is called
        func() #call the original function
        print("i am backend developer") #this will be printed after the original function is called
    return wrapper #return the wrapper function

def say_hello(): #this is the original function that we want to decorate
    print("Hello!") #this will be printed when the original function is called
    
say_hello = my_decorator(say_hello) #we apply the decorator to the original function, this will replace the original function with the wrapper function returned by the decorator
say_hello() #when we call the decorated function, it will execute the wrapper function, which will call the original function and add the additional behavior before and after it