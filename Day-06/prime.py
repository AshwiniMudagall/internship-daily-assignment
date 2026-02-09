num=int(input("Enter the number:"))
if(num<=1):
    print("not a prime")
else:
    flag=1
    for i in range(2,num):
      if(num%i==0):
         flag=0
         break
      
if(flag==1):
         print(f"{num} is a Prime number")
else:
             print(f"{num} is not a Prime number")