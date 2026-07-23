#f(x) = 3x + 2
#From this data wecan say x as Parameter and 3x + 2 as Argument

#Parameter is something defined in functions
#Argument is a value that is sent to the parameter when specified func is called

nama = input("Nama mu siapa? ")
def func(nama):
    print(f"Hello {nama}!")
#func() TypeError: func() missing 1 required positional argument: 'nama'
func(nama)

#POSITIONAL ARGUMENTS
