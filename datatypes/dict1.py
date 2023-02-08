#
# d = {}
# num = int(input('Enter the number of elements in the dictionary: '))
# for i in range(num):
#     key = int(input('Enter the key: '))
#     value = input('Enter the value: ')
#     d.update({key: value})
# print(d)

#
d = {1: 'red', 2: 'yellow'}
for i in d.keys():
    print(i)

#
for i in d.values():
    print(i)

#
for i, j in d.items():
    print(i, j)

#
x = d.get(2)
print(x)
