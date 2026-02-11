list=[]
num=int(input("Enter the size of the list"))
for i in range(num):
    n=input("Enter the element")
    list.insert(i,n)
    i+1
print(list)    
print(type(list ))