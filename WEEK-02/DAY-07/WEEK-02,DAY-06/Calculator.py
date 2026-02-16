
def addition(a,b,c):
    return a+b+c

def subtract(a,b,c):#results only positive difference
    if((a-b)>c):
     return a-b-c 
    else:
       return(c-(a-b))
   
    
def multiply(a,b,c):
    return (a*b*c)

def divide(a,b):
   return a/b

def modulus(a,b):
   return(a%b)

wish=int(input("Enter a number \n 1 for addition\n 2 for subttraction \n 3 for multiplication\n 4 for division\n 5 for modulus\n "))
if(wish==1):
   a=int(input("enter a number"))
   b=int(input("enter a number"))
   c=int(input("enter a number"))
   result=addition(a,b,c)
   print(f"{a}+{b}+{c}=",result)
    
elif(wish==2):
   a=int(input("enter a number"))
   b=int(input("enter a number"))
   c=int(input("enter a number"))
   result= subtract(a,b,c)
   print("Result:",result)

elif(wish==3):
   
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=int(input("enter a number"))
    
    
    result=multiply(a,b,c)
    print(f"Product of {a}*{b}*{c}:",result)
    
elif(wish==4):
   a=int(input("enter a number"))
   b=int(input("enter a number"))
   
   
   result=divide(a,b,c)
   print(f"Reminder of {a}/{b}:",result)

elif(wish==5):
   
    a=int(input("enter a number"))
    b=int(input("enter a number"))
   
    
    result=modulus(a,b)
    print(f"Reminder of {a}%{b}:",result)

print("Program Exceuted Successfully:")      
    


       