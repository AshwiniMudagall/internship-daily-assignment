num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
result = 0

while temp > 0:
    digit = temp % 10
    result += digit ** digits
    temp //= 10

if result == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

