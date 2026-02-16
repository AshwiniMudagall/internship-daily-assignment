f=open("file.txt","w+")
f.read()
print("File created")

with open("file.txt","w+") as f:
    f.write("Student Records\n")
    f.write("First Name=Ashwini\n")
    f.write("Last Name=Mudagall\n")

    f.write("Roll No.=76\n")

    f.write("Course=Bsc\n")
    f.write("Graduation Year=2027\n")
    f.write("Stream=Science\n")


    #reading file
with open("file.txt","r") as f:
     print(f.read())
   
