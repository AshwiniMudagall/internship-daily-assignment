str=input("Enter any string")
s=len(str)
print(s)
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")

