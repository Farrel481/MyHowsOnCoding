#How to insert data 2 json file though? 
#Well
#Watch me

import json

doxing = {
    "Name": "Farrel",
    "Alias": ["Grounder", "Rel", "Ano", "V"],
    "Age": 18,
    "Hobby": ["Love Multiplayer Story Games", "Sports", "Probably Gym", "I like CUddLEs"],
    "isMarried": False,
    "isHaveGf?": False
}

with open("c.json", "w") as file:
    json.dump(doxing, file)

with open("c.json") as file:
    cJson = json.load(file)
    print(cJson)
    print(type(cJson))
    print(cJson['Hobby'][0])