"""
Multiplication table using recursion
"""

def multiplicationTable(n, i):
    if i > 10:
        return
    print(n, '*', i, '=', n*i)
    return multiplicationTable(n, i+1)

print('Enter the number : ')
num = int(input())
print('\nMultiplication Table of', num, 'is: ')
multiplicationTable(num, 1)