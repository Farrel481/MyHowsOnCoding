#Use this to read Binary files.
#U can actually copy a picture this way.
#Printing it as text will surprise you.

with open("gbr.jpg", "rb") as file:
    binary = file.read()
    print(binary)

with open("gbrcopy.jpg", "wb") as file:
    file.write(binary)