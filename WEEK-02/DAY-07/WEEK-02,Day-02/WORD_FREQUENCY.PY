sentence=input("Enter any sentence")
frequency={}
words=sentence.split()
print(words)
for word in words:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print("Word Frequency:")     
for value in frequency  :
    print(value,"=",frequency[value]) 