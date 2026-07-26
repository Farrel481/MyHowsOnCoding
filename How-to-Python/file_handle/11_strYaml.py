#Gotta install library first
#Just do the pip drill
#pip install pyyaml
#py -m pip install pyyaml

import yaml

#Mapping is dict, sequence is list, scalar is the strintfloatbool.

#Convert str yaml to py datatypes
data = """
car: "Bayerische Motoren Werke"
age: 9 
owner: "Farrel Satriano"
"""

x = yaml.safe_load(data)
print(x)
print(x["car"], x["owner"])
print(type(x["age"]))
print(f"{x['owner']} is the owner of the beauty vellichor brand of {x['car']} for over {x['age']} years")

#convert py data to yaml

data = {
    "car": "BMW F10 535i",
    "engine": "N55B30",
    "Displacement": 3.0
}

x = yaml.dump(data)
print(x)
print(type(x))

#offed the default sorting
y = yaml.dump(data, sort_keys=False)
print(y)
print(type(y))


