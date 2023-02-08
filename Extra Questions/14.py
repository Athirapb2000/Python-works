"""
list comprehension with string list
"""

names = ['steve', 'bill', 'ram', 'mohan', 'abdul']
names1 = [s for s in names if 'a' in s]
print(names1)