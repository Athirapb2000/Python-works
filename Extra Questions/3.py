"""
check if two lists have common elements
"""

l1 = [1, 2, 4, 9, 6, 5]
l2 = [3, 5, 7, 8, 2]
print('List1: ', l1)
print('List2: ', l2)
l3 = []
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l3.append(l1[i])
if len(l3) == 0:
    print('no common elements')
else:
    print('List of common elements: ', l3)
