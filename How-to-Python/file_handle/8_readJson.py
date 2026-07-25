import json

with open("a.json") as file:
    a = file.read()
    print(a)
    print(type(a))
    #Change to it's realy py type
    aJson = json.loads(a)
    print(aJson)
    print(type(aJson))