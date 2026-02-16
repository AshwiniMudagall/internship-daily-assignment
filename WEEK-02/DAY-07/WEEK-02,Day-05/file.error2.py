try:
    f=open("MyFile2","r+")
    print(f.read())

except FileNotFoundError:
    print("The file as such does not exist:")