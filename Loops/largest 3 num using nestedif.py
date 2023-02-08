a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a > b:
    if a > c:
        print(a, 'is largest num among 3')
    else:
        print(c, 'is largest num among 3')
elif b > c:
    print(b, 'is largest num among 3')
else:
    print(c, 'is largest num among 3')
