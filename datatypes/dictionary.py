my_dict = {'Name': 'Athira', 'Age': '22', 'Address': 'abcd'}
print(my_dict)

print(type(my_dict))

print(my_dict['Age'])

print(my_dict.get('Name'))

print(my_dict.keys())

print(my_dict.values())

print(my_dict.items())

my_dict['Address'] = 'paramelpady'
print(my_dict)

my_dict.update({'Address': 'Paramelpady Street', 'Name': 'Athira PB'})
print(my_dict)

my_dict['Course'] = 'Python'
print(my_dict)

my_dict.pop('Address')
print(my_dict)

my_dict.popitem()  # pops the last item added in the dictionary
print(my_dict)

del my_dict['Age']
print(my_dict)

dict1 = {'Name': 'Athira', 'Age': 22, 'Address': 'abcd'}
print(dict1)
dict1.clear()
print(dict1)

dict2 = {'Name': 'Athira', 'Age': 22, 'Address': 'abcd'}
print(dict2)
for i in dict2.keys():
    print(i)
for i in dict2.values():
    print(i)

print(dict2.copy())
