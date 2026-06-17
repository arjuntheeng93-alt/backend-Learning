import json

data = {
    "users": [
        {"id" : 1, "name": "arjun", "role":"developer"}, 
        {"id" : 3, "name": "arrow", "role":"designer"}
        ]
    }
with open("day6/data.json", "w") as f:
    json.dump(data, f , indent=4)

with open("day6/data.json", "r") as f:
    loaded = json.load(f)
    print(loaded)
