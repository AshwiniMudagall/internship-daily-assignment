list=[22,46,87,50,75]
size=len(list)
even=0
odd=0
for i in range(size):
    
    if(list[i]%2==0):
         print(f"{list[i]} is even number")
         even+=1
    
        
    else:
        print(f"{list[i]} is a odd number")
        odd+=1

print("Total even number:",even)
print("Total odd number:",odd)