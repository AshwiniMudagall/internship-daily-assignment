#Creating and writing the file
f=open("myFile.txt","w")#As "w" creates a file 
print("File successfully created")
f.close()

#Appending in a file
with open("myFile.txt","a") as f:
 print(f.write("Hi this is Ashwini. "))

 print(f.write("I am learning file I/O in python.\n"))

 print(f.write("This is a important concept of python.\n "))
 f.close()

 #Read the file data 
 with open("myFile.txt","r") as f:
  data=f.read()
  print(data)
  f.close()

  #Storing the student information
  with open ("myFile.txt","a") as f:
   f.write("Name:Ashwini\n")
   f.write("Course:Bsc\n")
   f.write("Major Subject:Computer Science\n")
   f.write("Usn:U02AS24S0461\n")
   f.write("Age:20\n")

  print("File updated successfully with student details") 
