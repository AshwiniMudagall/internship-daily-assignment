str = "internship"
vowels = "aeiouAEIOU"
count = 0

for ch in str:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
