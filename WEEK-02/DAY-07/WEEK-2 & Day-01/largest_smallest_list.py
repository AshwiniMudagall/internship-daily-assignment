list=[]
num=int(input("Enyter the size of the list: "))
for i in range(num):
    n=input("enter the numbers ")
    list.insert(i,n)

print(list)

max=list[0] 
for i in range(num):
    if(list[i]>max):
        max=list[i] 
       
       
print(f"{max} is the largest number")

min=list[0]
for i in range(num):
    if(list[i]<min):
        min=list[i]
       
print(f"{min} is the smallest number")
print(type(list))    