#Writing and Appending
#mode write:
#1. if file does not exist, it'll make a new one and write.
#2. if the file does exist, it will overwrite it.

with open("unknown.txt", "w") as file:
    file.write("damn")
    #now check the file
