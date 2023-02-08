# Reverse
n = int(input('enter a number: '))  # 123
rev = 0
while n > 0:  # 123 > 0
    r = n % 10  # 123 % 10 = 3, 2, 1
    rev = rev * 10 + r  # 3, 32, 321
    n = n // 10  # 12, 1
print('Revere is: ', rev)

# Product
n = int(input('enter a number: '))
p = 1
while n > 0:
    r = n % 10
    p = p * r
    n = n // 10
print('Product is: ', p)

# Sum
n = int(input('enter a number: '))
s = 0
while n > 0:
    r = n % 10
    s = s + r
    n = n // 10
print('Product is: ', s)
