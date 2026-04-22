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