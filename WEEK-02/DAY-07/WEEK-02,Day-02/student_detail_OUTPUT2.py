group=set()
print(type(group))

group.add(43)
group.add(89)
group.add("Ashwini")
group.add("Mudagall")
group.add("Female")
print(group)
print("Length of the set",len(group))
print()

setts=set()
print(type(setts))
setts.add("Ashwini")
setts.add("Undergraduate")
setts.add(90)
setts.add(98)
print(setts)
print("Length of the set is:",len(setts))
print()


#OPERATIONS ON SET
#UNION
print("Union of two sets is:")

print(group.union(setts))
print("Length of union of sets:",len(group.union(setts)))
print()

#INTERSECTION OF TWO SETS
print("intersection of two sets is:")

print(group.intersection(setts))
print("Length of the intesected sets is ",len(group.intersection(setts)))
print()
#DIFFERENCE OF TWO SETS
print("Difference of two sets is:")

print(group.difference(setts))#Elements in groups but not setts 
print("Length of the set is",len(group.difference(setts)))
print()


#Symmetric difference
print("Symmetric difference of two sets is:")#Elemnts that are either in group or setts but not in both 
print(group.symmetric_difference(setts))
print("Length of the set is",len(group.symmetric_difference(setts)))