list=[]
num=int(input("Enter the size of the list: "))

for i in range(0,num):
    n=input("Enter the elements: ")
    list.insert(i,n)

print(list)

list.sort()
print("List in ascending order:")
print(list)

list.sort(reverse=True)
print("list in descending order:")

print(list)