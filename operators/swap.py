# using temporary variable

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('before swapping: ', a, b)
t = a
a = b
b = t
print('after swapping: ', a, b)

# without using temporary variable

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('before swapping: ', a, b)
a = a + b
b = a - b
a = a - b
print('after swapping: ', a, b)

# simple way

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('before swapping: ', a, b)
a, b = b, a
print('after swapping: ', a, b)
