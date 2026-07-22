#Writing and Appending
#mode write:
#1. if file does not exist, it'll make a new one and write.
#2. if the file does exist, it will overwrite it.

with open("unknown.txt", "w") as file:
    file.write("damn")
    #now check the file

#mode append:
#1. just the same but if you already have the file, it will not overwrite, it will write on next index instead.
#Here I already have "new" file filled with 1 + 1 = 2
with open("new.txt", "a") as file:
    file.write(" Wow, u good at math?")
    #check it!

