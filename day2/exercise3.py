def multiply(x,y):
    return x * y
def apply(func, a,b):
    return func(a,b)

result = apply(multiply, 3, 4)
print(result)