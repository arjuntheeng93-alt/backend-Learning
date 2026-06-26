#today i am learning about super()
#super() calls the parent class method used when a child class wants to extended the parent not completely replace it 

class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Dog(Animals):
    def __init__(self,name, age, breed):
        super().__init__(name, age) # call Animal.__init__
        self.breed = breed
        
animals = [Dog("husky",22,"Seto")]
for animal in animals:
    print(f"Name: {animal.name}, Age: {animal.age}, Breed: {animal.breed}")    
    
#without super()you had have to repeat self.name = name and self.age = age in every child class that duplicate code which is bad practice