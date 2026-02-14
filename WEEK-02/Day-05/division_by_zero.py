try:
 num=int(input("Enter a number "))
 result=num/0

except ZeroDivisionError:
 print("Error:Please enter an integer other than zero")