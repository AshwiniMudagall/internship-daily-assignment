str=input("Enter any word:")
frequency=0
char_freq={}
for ch in str:
   if ch in char_freq:
      char_freq[ch]+=1
   else:
      char_freq[ch]=1
print("Character Frequency:")
for ch in str:
   print(ch,"=",char_freq[ch])