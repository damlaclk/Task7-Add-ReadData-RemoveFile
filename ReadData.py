readFile = input("Enter File Name: ")
readData = open(readFile, "r") #"r" - Read is the default, opens the file for reading. If the file does not exist, it gives an error.
print(readData.read())
