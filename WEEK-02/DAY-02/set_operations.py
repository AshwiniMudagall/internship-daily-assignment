
#CREATING A SET
group=set()
group.add(2)
group.add(34)
group.add(56)
group.add("Ashwini")
group.add("Mudagall")
group.add("Hubli")
print(group)
print(type(group))
print("Length of the group :",len(group))
print()

#CREATING SET-2
setts=set()
setts.add(67)
setts.add("Ashwini")
setts.add(89)
setts.add("Hubli")
print(setts)
print(type(setts))
print("Length iof the setts :",len(setts))
print()

#OPERATIONS ON SET
#UNION OF SETS
print(group.union(setts))
print("Length of the set after union:",len(group.union(setts)))
print()

#INTERSECTION OF SETS
print(group.intersection(setts))
print("Length of the set after intersection:",len(group.intersection(setts)))
print()

#DIFFERENCE OF TWO SETS
print(group.difference(setts))#return the elements in group but not in setts
print("Length of the set after differnce:",len(group.difference(setts)))
print()

#SYMMETRIC DIFFERENCE OF TWO SETS 
print(group.symmetric_difference(setts))
print("Length of the set after the symmmetric difference:",len(group.symmetric_difference(setts)))
print()