import os

removeFile = input("Enter The File Name: ")

if os.path.exists(removeFile): #os.path.exists() method is used to check whether the specified path exists or not. 
	os.remove(removeFile)
	print("The file has been deleted.")
else:
	print("This file was not found.")
