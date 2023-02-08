"""
write a program to extract numbers from a string by using list comprehension
"""
string = 'the room number 45 and 67 are vaccant'
new = [x for x in string if x.isdigit()]
print(new)