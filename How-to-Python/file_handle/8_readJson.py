import json

with open("a.json") as file:
    a = file.read()
    print(a)
    print(type(a))
    #Change py list
    aJson = json.loads(a)
    print(aJson)
    print(type(aJson))

#Open and immediately read as py list
with open("a.json") as file:
    aJson = json.load(file)
    print(aJson)
    print(type(aJson))

with open("b.json") as file:
    bJson = json.load(file)
    print(bJson)
    print(type(bJson))
    print(bJson['name'])
    print(bJson['age'])
    print(bJson['isMarried'])
    print(bJson['Friends']['Male'])
    print(bJson['Friends']['Female'])
    print(bJson['Friends']['Male'][2])
    print(bJson['Friends']['Female'][0])

print("Fuck you Joel.")
print("I LOVE JANE DOEEE ARGH")