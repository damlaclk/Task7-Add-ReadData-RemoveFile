name = input("Enter Your Name: ")
surname = input("Enter Your Surname: ")
email = input("Enter E-mail Address: ")

ourFile = open("data.txt", "a") # "a" - Append opens the file to add data, creates a new one if the file does not exist
ourFile.write("\n"+ "Name:" + name + " Surname:" + surname +  " Email Address:" + email)
