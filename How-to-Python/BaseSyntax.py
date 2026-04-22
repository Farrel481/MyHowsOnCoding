#Printing
print("Hello World")
print('Hello \nEveryone!')
print('Hello' + 'Farrel')
print("Kota", 'Bandung', "Barat")
print("Kota", 'Jakarta', "Selatan", sep="-")

print("Satu"
      "Dua"
      "Tiga")

#Variable
name = "Farrel"
age = 17

print("Hello ", name, ", Kamu apakabar?")
print("Hello " + name + ", Kamu apakabar?")
print(f"Hello {name}, Kamu apakabar?")
print("Hello {}, Kamu apakabar?".format(name))
#Bisa juga kaya bahasa C/C++ nih
print('Hello %s, Umur kamu %d tahun ya?' % (name, age))

teks = "Hello World!"
print(teks.upper())
print(teks.lower())
print(teks.split())
print(teks.replace("World", "Everyone"))

#Operators

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3) #Floor Division
print(10 % 3) #Modulus
print(10 ** 3) #Exponentiation

#Assignment Operators
name = "Andi"
number = 26
total = number + 5
print(total)

x, y = 10, 20
x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)

#Logical Operators
a = True
b = False

x, y = 10, 20
print(x < 10 and y > 5)
print(x < 10 or y > 15)
print(not(x < y))

#Identity Operators
x = 10
print(x is 5)
print(x is not 5)
y = 35
print(x is y)
print(x == y)
