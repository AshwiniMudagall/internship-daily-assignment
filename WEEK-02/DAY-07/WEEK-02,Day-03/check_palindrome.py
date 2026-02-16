str=input("Enter a string ")
rev_str=" "
for i in range(len(str)-1,-1,-1):
    rev_str+=str[i]
print(rev_str)
if(str==rev_str)  :
    print(" Palindrome")
else:
    print(" not a palindrome")  
