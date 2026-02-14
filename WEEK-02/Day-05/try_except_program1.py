#Try-Except Program
try:
 #num=int(input("Enter a number"))
 #print(num2)
 #num=input("Enter a number")
 #q="p"
 #result=num/q
 num="three"
 print(num.capital())

 

except TypeError: #It will raise if the particular operation cannot be performed on a specific type of inpput data
 print("Type Error:")
 
except ValueError:#raised when input  value does not match the required input type though the type is correct
   print(" Value Error: Entered type is not integer value")

except NameError:#raised when called a name that is not defined
   print("Name Error: There is no such element defined")

except AttributeError:#raised when calling a method that does not exist
  print("Attribute Error: There is no such attributes or methods defined:")

except SyntaxError:#raised when there is syntactical mistakes in the code 
  print(" Syntax Error: Please check the code as there is some syntax mistake:")

   
print("Program reached the end:")
