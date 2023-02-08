tpl = ('apple', 'banana', 1, 7, 2.5)
print(tpl)
print(type(tpl))

lst = ['apple', 'banana', 1, 7, 2.5]
print(lst)
print(tuple(lst))                                   # changing any datatype into tuple

tpl = ('apple', 'banana', 1, 7, 2.5, 'apple', 7)    # allow duplicates
print(tpl)

tpl = ('meenu', 1, 5, ('athira', 'aparna'), 'sneha', (3, 7, 1))
print(tpl)
print(len(tpl))                                     # length of the tuple

print(tpl[0])                                       # indexing
print(tpl[-1])
print(tpl[1:3])
print(tpl[1:-1])
print(tpl[::-1])                                    # reverse of a tuple
print(tpl[:-5])
print(tpl[-4:-1])

# to update a tuple
y = list(tpl)
y[0] = 'Kunju'
tpl = tuple(y)
print(tpl)

# append
x = list(tpl)
x.append('praseetha')
tpl = tuple(x)
print(tpl)

z = list(tpl)
z.append((8, 9))
tpl = tuple(z)
print(tpl)

# remove
z.remove((8, 9))
tpl = tuple(z)
print(tpl)

# del
# new_tuple = (1, 2, 3, 4, 5)
# del new_tuple
# print(new_tuple)

# unpacking a tuple
fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ('apple', 'mango', 'papaya', 'pineapple', 'cherry')
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = ('apple', 'banana', 'cherry')
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# functions in tuple
'''
all()
any()
enumerate()
len()
max()
min()
sorted()
sum()
tuple()
'''

# nested tuple accessing
n_tple = ('ATHIRA', [1, 2, 3], (4, 5, 6))
print(n_tple[0])
print(n_tple[1])
print(n_tple[0][0])
print(n_tple[1][0])
n_tple[1][1] = 23
print(n_tple)
# n_tple[0][1] = "C"
# print(n_tple)

# concatenation
print((1, 2, 3) + (4, 5, 6))

# repeat
print(('repeat',) * 3)

my_tuple = ('a', 'p', 'p', 'l', 'e')
print('Total count of element p is', my_tuple.count('p'))       # count
print('index of l is', my_tuple.index('l'))                     # index

print('a' in my_tuple)
print('b' in my_tuple)
print('g' not in my_tuple)

names = ("Athira", "Aparna", "Sneha")
for name in names:
    print('Hello', name)

t1 = (1, 2, 3, 4, 5)
print(all(t1))
t2 = (1, 2, 3, 'athira')
print(all(t2))
t3 = (1, 2, 3, 'true')
print(all(t3))
t4 = (0, 1, 2, 3, 'false')
print(all(t4))

# functions
a = (4, 2, 8, 5, 1, 4)
print(len(a))
print(all(a))
print(min(a))
print(max(a))
print(sorted(a))
print(sum(a))

x = ('python', 'java', 'express')
y = enumerate(x)
print(tuple(y))

letters = [('a', 'A'), ('b', 'B')]
for i, letters in enumerate(letters):
    print('Letter #%d is %s/%s' % (i, letters[0], letters[1]))

names = ('athira', 'aparna', 'sneha')
ages = (22, 20, 23)
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

lm = ['sat', 'bat', 'cat', 'mat']
test = list(map(tuple, lm))
print(test)
