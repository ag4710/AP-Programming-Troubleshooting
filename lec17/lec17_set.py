odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
emptyset = set() # {} creates an empty dictionary
randomset = {4, 6, 2, 7, 5, 2, 3} # Duplicated ele.
print(odds)
print(evens)
print(emptyset)
print(randomset)
print()

gold = [0, 4, 5, 10, 3, 0, 2, 1, 4, 8, 1, 0, 1,
0, 0, 8, 11, 4, 13, 1, 2, 3, 2, 6, 1, 9]
print(gold)
goldset = set(gold)
print(goldset)
print(type(goldset))
print()

print(set("Good morning!"))
print()

print(3 in odds )
print(2 in odds )
for num in odds:
    print(num)
print()

print(randomset)
randomset.add(9)
print(randomset)
randomset.remove(7)
print(randomset)
print(randomset.pop())
print(randomset)
print()

randomset.intersection(odds)
print(randomset)
randomset.union(evens)
print(randomset)
randomset.difference(odds)
print(randomset)
odds.difference(randomset)
print(odds)
randomset.difference(odds, evens)
print(randomset)