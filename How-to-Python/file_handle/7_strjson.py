import json

#JSON data format to str
data = '{"name": "Farrel", "city": "Unknown"}' #most will miss the " ' ".
print(data)
print(type(data))

dataJson = json.loads(data) #str json as an object equals py dict
print(dataJson)
print(type(dataJson))

data2 = '[12, 24, 48, 96, 192]' #str json as an array equals py list
data2Json = json.loads(data2)
print(data2Json)
print(type(data2Json))

data3 = '{"count": [1, 2, 3]}'
data3Json = json.loads(data3)
print(data3Json)
print(type(data3Json))

data4 = '[1, 2, {"Me": "Myself"}]'
data4Json = json.loads(data4)
print(data4Json)
print(type(data4Json))

#Invalid Json variable
#data5 =  '{"name": "Agus", "age": 21, "0": true, "x": null,}'
# data5Json = json.loads(data5)
# print(data5Json)
# print(type(data5Json))

#Dict or List to str JSON

a = [1, 2, 3, 4, 5, 'Farrel']
print(a)
print(type(a))

aJson = json.dumps(a)
print(aJson)
print(type(aJson))

b = {
    "name": "Farrel",
    'age': 18,
    18: True,
    "x": None
}

bJson = json.dumps(b)
print(bJson)
print(type(bJson))