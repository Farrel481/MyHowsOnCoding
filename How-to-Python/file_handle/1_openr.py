#open("namafile.ext", "mode")
#r = read, w = write, a = append, r+ = read & write.
#additional modes : t = text, b = binar (for images usually)

file = open("test.txt", "r")
print(file.read()) #read all content
file = open("test.txt", "r")

line1 = file.readline()
print(line1)
line2 = file.readline()
print(line2)

#1. Remember to handle exceptions

try:
    file = open("test2.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError as error:
    print(f"ERROR: {error}")

#2 Better way for modern code
try:
    with open("test2.txt", "r") as file:
        print(file.read())
except FileNotFoundError as error:
    print(f"ERROR: {error}")

#Trying with non-existent file
try:
    with open("cauhaseum.txt", "r") as file:
        print(file.read())
except FileNotFoundError as error:
    print(f"ERROR: {error}")

#If u only want for answer in a list form
with open("test.txt", "r") as file:
    lines = file.readlines() 
    print(lines)
    
#3. File path location
try:
    with open("foldertesting/Plu.txt", "r") as file:
        print(file.read())
except FileNotFoundError as error:
    print(f"ERRORR: {error}")

#can do backward paths too.
    with open("../second.txt", "r") as file:
        print(file.read())

#4. Open() files methods
with open("test2.txt", "r") as file:
    text = file.read()
    print(text)
    print(text.find("Nut"))

    file.seek(0) #Move Cursor to first char, output from first char.
    print(line1)
    file.seek(3) 
    line1 = file.readline()
    print(line1)