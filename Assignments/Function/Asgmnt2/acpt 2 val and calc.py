# 8.define a function that accepts 2 values and return its sum,subtraction and multiplication
def calc(x, y):
    print('sum is', x+y)
    print('difference is', x-y)
    print('product is', x*y)
    return x + y, x - y, x * y
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
calc(n1, n2)
