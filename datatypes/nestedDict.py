dict1 = {1: {'Name': 'Athira PB', 'Age': 22, 'Course': 'Python'},
         2: {'Address': 'Paramelpady Street', 'Class': 'MCA'}}
print(dict1)
print(dict1[1]['Name'])
print(dict1[2])
dict1[3] = {'fruit1': 'apple', 'fruit2': 'orange'}
print(dict1)
print(dict1.get(1))
print(dict1[2].get('Class'))
dict1[2]['Address'] = 'Paramelpady'
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1.update({4: {'friend1': 'Sneha', 'friend2': 'Aparna'}, 5: {'sister': 'Kunju'}})
dict1.popitem()
print(dict1)
dict1.pop(2)
print(dict1)
