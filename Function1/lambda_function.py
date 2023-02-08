def sum(a, b):
    return a+b
print(sum(10, 20))

# syntax= lambda arguments:expression
add = lambda a, b: a+b
print(add(2, 3))

#
largest = lambda a, b: a if(a > b) else b
print(largest(59, 34))

# filter
l = [2, 5, 10, 50, 77, 34]
lst = list(filter(lambda x: x % 2 == 0, l))
print(lst)

# map
l = [2, 5, 10, 50, 77, 34]
lst = list(map(lambda x: x > 10 == 0, l))
print(lst)

# reduce
from functools import reduce
l1 = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, l1)
print(product)

# diff btw lambda and user defined function