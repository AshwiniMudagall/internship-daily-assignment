try:
    with open("MyFile.txt","r") as f:
        data=f.read()

except IOError:
 print("Please ensure the files exist")