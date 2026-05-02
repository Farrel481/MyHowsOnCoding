#OOP is simply Object Oriented Programming.
#Artinya OOP itu programming yang terfokus pada sebuah object atau tujuan tertentu.

#Today Commit at 28/04/2026 we will learn about class

#Class Static
class Binatang:
    jumlahKaki = 4          #properti
    habitat = 'Darat'       #properti  
    def suara(self):        #method dan self ini a must untuk first parameter
        return 'Mengaum'

anjing = Binatang()
print(anjing.jumlahKaki)
print(anjing.habitat)
print(anjing.suara())

kucing = Binatang()
print(kucing.jumlahKaki)
print(kucing.habitat)
print(kucing.suara())

#Contoh penggunaan yang salah
elang = Binatang()
print(elang.jumlahKaki) 
print(elang.habitat)
print(elang.suara()) 


class kelasKosong:
    pass

o = kelasKosong()
print(o)

class Player:
    name = 'Andi'
    def run(self):
        return f"run {self.name}"
    
#Abstracion of real Objects:
class SUV:
    engine = 2500
    power = 180
    length = 4.9
    height = 1.9
    transmission = "A/T"
    brand = "Mitsubishi"
    seat = 7

pajero = SUV()
print(pajero.engine)

'''
class animal: #Ini adalah abstract class

class kucing: #Ini adalah isi dari abstract class
    
class unggas: #Ini adalah isi dari abstract class
    '''