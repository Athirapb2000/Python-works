dict1 = {'MATHS': 87, 'SCIENCE': 90, 'ENGLISH': 95, 'MALAYALAM': 100}
print('*****************************\nSUBJECT\t\t\t\t\tMARKS\n*****************************')
for key, value in dict1.items():
    if key == 'MATHS':
        print(key, '\t\t\t\t\t', value)
    else:
        print(key, '\t\t\t\t', value)
