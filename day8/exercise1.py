class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "..."
    
    def __str__(self):
        return f"{self.__class__.__name__}(name= {self.name})"
    
class dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class cat(Animal):
    def speak(self):
        return f"{self.name} say meow!"

animals = [dog("husky"), cat("Whiskers")]
for animal in animals:
    print(animal)
    print(animal.speak())