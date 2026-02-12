str=input("Enter any string:")
vowels=0
consonant=0
vowel_letter="aeiou"
for char in str:
    if char in vowel_letter:
      vowels+=1
else:
    consonant+=1

print("The total number of vowels are:",vowels)
print("The total number of consonants are:",consonant)

