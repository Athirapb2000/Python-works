"""
1. immutable
2. unordered
3. unindexed
4. duplicates not allowed

Set items are unchangable, but you can remove and add items.
"""
set1 = {1, 2, 3, 4, 5}
print(set1)
set2 = {1.0, 2, 4, 'Hello', (1, 2, 3)}
print(set2)
a = set([1, 2, 3, 4])
print(type(a))

A = {1, 2, 3, 0, 5, 7}
B = {2, 5, 8, 6, 9, 4}
print(A | B)            # union
print(A & B)            # intersection
print(A - B)            # difference
print(A ^ B)            # symmetric difference

# 1.add a list of elements to a set
set1 = {1, 'athira', 6, (1, 7)}
list1 = [5, 0, 4]
set1.update(list1)
print(set1)

# 2.get only unique items from two sets
A = {1, 2, 3, 5, 7}
B = {6, 7, 1, 3, 5}
print(A | B)

# 3.check if two sets have any elements in common. if yes, display the common elements
A = {1, 2, 3, 5, 7}
B = {6, 7, 1, 3, 5}
A.intersection(B)
print(A)

# 4.remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.difference_update(set2)
print(set1)
