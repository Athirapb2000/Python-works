# syntax: list=[expression for item in list if condition]

l = [x+3 for x in [1, 2, 3]]
print(l)

#
l = [i for i in range(25) if i % 2 == 0]
print(l)

# vowels
v = [i for i in 'hai how are you?' if i in ['a', 'e', 'i', 'o', 'u']]
print(v)

#
colors = ['red', 'white', 'black', 'pink', 'green']
newlst = [i for i in colors if 'e' in i]
print(newlst)

#
colors = ['red', 'white', 'black', 'pink', 'green']
newlst = [i for i in colors if i != 'green']
print(newlst)

#
colors = ['red', 'white', 'black', 'pink', 'green']
newlst = [i.upper() for i in colors]
print(newlst)

#
colors = ['red', 'white', 'black', 'pink', 'green']
newlst = ['hello' for i in colors]
print(newlst)

#
colors = ['red', 'white', 'black', 'pink', 'green']
newlst = [i if i != 'pink' else 'blue' for i in colors]
print(newlst)