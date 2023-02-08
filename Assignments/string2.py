# 1.Replace each special symbol with # in the following string
str1 = "/*Jon is @developer & musician!!"
special_chars = ['/', '*', '@', '&', '!']
for i in special_chars:
    str1 = str1.replace(i, '#')
print(str1)
print('\n')

# 2. Append new string in the middle of a given string. output: LumPythoninar
s1 = 'Luminar'
s2 = 'Python'
str_len = len(s1)
mid_index = str_len//2
s3 = s1[0:mid_index]
s4 = s3 + s2
new_str = s4 + s1[mid_index:str_len]
print(new_str)
