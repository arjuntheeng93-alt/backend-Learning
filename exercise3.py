import json
class JSONFileStore: #WE MAKE A CLASS CALLED JSONFILESTORE
    def __init__(self, filepath): #this method run automatically when the class is called
        self.filepath = filepath#we create attribute inside the object
        self.data = {} # we create an empty dictionary
        
    def __enter__(self): # we wil setup before the code inside the with block runs / enter preaper the object before we use it
        try: # we use try method to prevent from error
            with open(self.filepath, 'r') as f: # then we open file in read mode
                self.data = json.load(f)#  id file exist it will load as a json
        except FileNotFoundError:# if not then it will get empty dictionary
            self.data = {}
        return self #it become the variable as store self = store
    
    def __exit__(self, exc_type, exc_val, exc_tb):# it run automatically when leaving the block
        with open(self.filepath, "w")  as f: #create or over write the file
            json.dump(self.data, f, indent = 4)# dump save/write data to a file , self.data is our dictionary, f file where the data is saved and indent make our json organized
            
            
    def get(self, key):  #get a value
        return self.data.get(key)
    
    def set(self, key, value):# the we add or update value
        self.data[key] = value
    
    def delete(self, key): # it prevent from error when the key is empty
        self.data.pop(key, None)

with JSONFileStore("day6/store.json") as store:# we use clss
    store.set("name", "Arjun")
    store.set("role", "developer")
    print(store.get(("name")))

with JSONFileStore("day6/store.json") as store:
    print(store.get("name"))
    print(store. get("role"))
    store.delete("role")
    
with JSONFileStore("day6/store.json") as store:
    print(store.get("role"))