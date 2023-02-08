"""
Write a prgm to print characters from a string that are present at an even ndex number
"""

str1 = input('Enter a string: ')
l = len(str1)
print('Characters at even index number are: ')
for i in range(0, l, 2):
    print(str1[i])
