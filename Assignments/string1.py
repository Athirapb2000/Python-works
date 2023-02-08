# 1.how would you check if each word in a string begins with a capital letter
str1 = "Welcome to Luminar Technolab"
print(str1)
print(str1.istitle())
print(str1.title())
print('\n')

# 2.check if a string contains a specific substring
str1 = "Python Programming"
if 'gram' in str1:
    print("it contains gram\n")
else:
    print("it does not contain gram\n")

# 3.find the index of the first occurence of a substring in a string
str1 = 'Hello World'
print((str1.find('llo')))
print('\n')

# 4.count the total no.of characters in a string
txt = 'athira'
print(len(txt))
print('\n')

# 5.count the no.of a specific character in a string
ch = 'aparna'
b = ch.count('a')
print(b)
print('\n')

# 6.capitalize the first character of a string
ch = "sneha"
print(ch.capitalize())
print('\n')

# 7.check if a string contains only numbers
a = 'athira'
print(a.isdigit())
b = '123'
print(b.isalnum())
print('\n')

# 8.split a string on a specific character
ch = 'athirababy'
print(ch.split('a'))
print('\n')

# 9.reverse the string "hello world"
txt = 'hello world'
print(txt[::-1])
print('\n')

# 10.join a list of strings into a single string,delimited by hyphens
s = ['apple', 'banana', 'grapes']
print("-".join(s))
print('\n')

# 11.give an example of  string slicing
txt = 'python'
print(txt[0:3])
print(txt[0:-1])
print(txt[:0:-2])
print('\n')

# 12.convert an integer to string
str2 = 5
print(str(str2))
print('\n')

# 13.replace all instances of a substring in a string
str4 = 'aathiraa'
print(str4)
print(str4.replace('aa', 'a'))
print('\n')

# 14.remove whitespace from the left,right or both sides of a string [lstrip() ,rstrip(), strip()]
str5 = ' hello athira '
print(str5)
print(str5.lstrip())
print(str5.rstrip())
print(str5.strip())
print('\n')

# 15.what does it mean for strings to be immutable in python
""" string is immutable because we cannot make any changes in the string. """
