

lst = [1, 2, 90, 65, 74]
max_val = lst[0]
size = len(lst)

for i in range(size):
    if lst[i] > max_val:
        max_val = lst[i]

print(f"{max_val} is the largest number")
print("Program executed successfully")