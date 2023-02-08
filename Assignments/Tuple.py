# 1.convert a string to tuple
str1 = 'Python Programming'
tpl = tuple(str1)
print(tpl)

# 2.convert list to tuple
lst = [1, 7, 'athira']
tpl = tuple(lst)
print(tpl)

# 3.find repeated items from a tuple
tpl = (1, 6, 4, 1, 8, 5, 4)
print('Tuple', tpl)
z = set()
for i in tpl:
    if tpl.count(i) > 1:
        z.add(i)
print(f'Repeated elements in tuple {tuple(z)}')

# 1.reverse a tuple
tp = ('a', 'b', 9, 5, 'h')
new_tp = tuple(reversed(tp))
print(new_tp)

# 2.remove repeated elements from tuple
tpl = (1, 2, 40, 40)
a = []
for element in tpl:
    if element not in a:
        a.append(element)
print(tuple(a))

# access the value 20 from the tuple
tpl = (1, 2, 40, 20, [10, 2, 30], (30, 20, 10), 40)
if 20 in tpl:
    print(20)
else:
    print('invalid')

# 3.check if all items in the tuple are same
tpl = (1, 2, 40, 30, 20)
if tpl[0] * len(tpl) == tpl:
    print("Equal")
else:
    print("not equal")

# OR
tup = (1, 1, 40, 30, 20)
# tup = (1, 1, 1, 1)
f = 1
for i in tup:
    for j in range(i, len(tup)-1):
        if tup[i] != tup[j+1]:
            f = 0
            break
if f == 1:
    print('same')
else:
    print('not same')

# 4.copy specific elements from one tuple to a new tuple
tpl = (1, 2, 3, 4, 5, 6, 7, 8)
y = tpl[2:5]
print(y)

# 5.swap two tuples in python
a = (1, 6)
b = (5, 4)
print('Before swap A :', a)
print('Before swap B: ', b)
temp = a
a = b
b = temp
print('After swap A :', a)
print('After swap B: ', b)
