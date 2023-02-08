"""
write a program to print integer values in a list using list comprehension
"""

ls = [12, 66, 14.5, 12.8, 12, 2.4, 11, 22]
result = [x for x in ls if type(x) == int]
print(result)