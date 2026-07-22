#Copy a file this way.

with open("new.txt", "r") as file:
    var1 = file.read()

with open("copy.txt", "w") as file:
    print(var1)