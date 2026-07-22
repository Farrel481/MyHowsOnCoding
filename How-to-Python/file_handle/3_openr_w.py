#With this mode, you can read and write at the same time.
#So then u can check without having 2 open file.
#But this file will not make a new one if the file does not exist.
#So use exception FileNotFoundError!
#This mode overwrites. Use a variable and seek to append.

try:
    with open("pisangcau.txt", "r+") as file:
        text = file.read()
        file.seek(0)
        file.write("Baru tau gua!")
        file.write(text)
except FileNotFoundError as error:
    print(f"FileNotFoundError in {error}")

with open("pisangcau.txt", "r") as file:
    text = file.read()
    print(text)

try: #will fail
    with open("Lmao.txt", "r+") as file:
        text = file.read()
        file.seek(0)
        file.write("Baru tau gua!")
        file.write(text)
except FileNotFoundError as error:
    print(f"FileNotFoundError in {error}")