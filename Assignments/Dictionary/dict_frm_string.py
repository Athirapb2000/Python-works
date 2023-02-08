str1 = 'Luminar'
print('The given string is: ', str1)
dict1 = {}
for index in range(1, len(str1)+1):
    dict1.setdefault(index, str1[index-1])
print('The corresponding dictionary of the given string is: ', dict1)

# OR
for i in range(1, len(str1)+1):
    dict1.update({i: str1[i-1]})
print(dict1)
