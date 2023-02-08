# sum of 2 numbers
def sum(a, b):
    print('sum is :', a+b)
sum(5, 6)

# square of 2 no.s
def square(num):
    return num**2
obj = square(5)
print(obj)

# find the max of 3 numbers
def maxm():
    l1 = [1, 5, 3, 9, 4]
    a = max(l1)
    return a
print(maxm())

# sum all the numbers in a list
def listSum():
    s = 0
    for i in l2:
        s = s + i
        i += 1
    return s
l2 = [1, 2, 3, 4, 5]
print(listSum())

# multiply all the numbers in a list
def mul(l3):
    r = 1
    for i in l3:
        r = r * i
        i += i
    return r
print(mul(l3=[1, 2, 3, 4]))
