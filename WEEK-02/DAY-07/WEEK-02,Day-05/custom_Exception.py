class Own_Exception(Exception):
    pass



try:
   count=int(input("Enter a number:"))
   if(count<0):
    raise Own_Exception
   
   else:
      print("The value is",count)

except Own_Exception:
    print("The count cannot be negative")
