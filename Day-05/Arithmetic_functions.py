#ADDITION
#Default values of a & b is 1,1
def add(a=1,b=1):
    sum=a+b
    print("Sum is",sum)
    return sum

#SUBTRACTION(positive difference)
#Default values of a & b is 1,0
def subtract(a=1,b=0):
   while(a>b):
       diff=a-b
       print("Positive difference is:",diff)
       break
   else:
       print("a is less than b")

       #Negative differece
       #Default values of a & b is 1,2
       def subtract1(a=1,b=2):
           diff=a-b
           while(a<b):
               print("Negative difference is:",diff)
               break
               return diff
           
#MULTIPLICATION
#Default values of a,b,c is 1,1,1
def product(a=1,b=1,c=1):
    multiply=a*b*c
    print("Product is ",multiply)
    return product

#DIVISION
#Default values of a & b is 1,1
def divide(a=1,b=1):
    division=a/b
    print("The quotient is:",division)
    return division

#MODULOUS
#Default values of a & b is 4,2
def modulo(a=4,b=2):
    modulus=a%b
    print("The reminder is:",modulus)
    return modulus


add()
add(654,756)
subtract()
subtract(780,80)
product()
product(9,6)
divide()
divide(63,9)
modulo()
modulo(34,2)
