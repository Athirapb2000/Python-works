"""
REGULAR EXPRESSION
    It can be used to check if a string contains the specified search pattern.
    Python has a builtin package 're' which can be used to with regular expression.
    There are 4 methods in regular expression
    1. findall() - It returns a list containing all matches
    2. search() - It returns a match object if there is a match anywhere in the string
    3. split() - splits the input(character, string, numbers etc..)
    4. sub() - It replaces one or many matches with a string(replace or substitute)
"""

"""
findall()
"""

import re
str = 'rose is a beautiful and colorful flower'
s = re.findall('ful', str)
print(s)
s1 = re.findall('full', str)
print(s1)

# []
d = 'cat mat sat rat pat'
a = re.findall('[scr]', d)
print(a)

d = 'cat mat sat rat pat'
a = re.findall('[sc]a', d)
print(a)

d = 'cat mat sat rat pat'
a = re.findall('[scrm]at', d)
print(a)

# [^]
d = 'cat mat sat rat pat'
a = re.findall('[^scr]', d)
print(a)

# \d{}
d = 'cat mat sat rat pat 78976 999'
a = re.findall('\d{3}', d)
print(a)

d = 'cat mat sat rat pat 78976 999'
a = re.findall('\d{1,3}', d)
print(a)

d = 'cat mat sat rat pat 78976 999 6666'
a = re.findall('\d{2,3}', d)
print(a)

d = 'cat mat sat rat pat 78976 999 6666'
a = re.findall('\d{2,4}', d)
print(a)

# \b\d{}\b
d = 'cat mat sat rat pat 78976 999 6666'
a = re.findall(r'\b\d{4}\b', d)
print(a)

"""
search()
"""

str = 'class will start at 10am'
s = re.search('\s', str)
print(s)
print(s.start())

s1 = re.search('\d', str)
print(s1.start())

s2 = re.search('python', str)
print(s2)

str = 'class will start at 10am'
s = re.search('^class.*10am$', str)
print(s)
if s:
    print('find')
else:
    print('not find')

"""
split()
"""

str = 'class will start at 10am'
s = re.split(' ', str)
print(s)

s1 = re.split('a', str)
print(s1)

s2 = re.split(' ', str, 2)
print(s2)

str = 'Version are python1 python2'
b = re.fullmatch(str, 'python\d')
print(b)

"""
sub()
"""

input = 'rose and jasmine are flowers'
g = re.sub(' ', '*', input)
print(g)

g = re.sub(' ', '*', input, 3)
print(g)

# mail validations
import re
regexp = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[w.]{2,3}$'
def check(email):
    if re.search(regexp, email):
        print('valid email')
    else:
        print('invalid email')

if __name__ == '__main__':

    email = 'athira.pb@jmc.net'
    check(email)

    email = 'aparna@pb-jcet.com'
    check(email)

    email = 'sneha30cp@gmail.com'
    check(email)

    email = 'athirapb21@gmail.com'
    check(email)