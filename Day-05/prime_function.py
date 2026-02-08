

def check_prime(a):
     flag=1#assume a is prime
     for i in range(2,a-1):
      
       if(a%i==0):
           flag=0#a is not prime
           break
     if (flag==1):
         print(f"{a} is  prime")
     else:
         print(f"{a} is  not prime")
check_prime(4)