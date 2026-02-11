list=[]
num=int(input("Enter the size of list:"))
for i in range(0,num):
    n=input("enter elements:")
    list.insert(i,n)
print(list)
print(type(list))

tup=tuple(list)
print("List converted into a tuple:")
print(tup)
print(type(tup))