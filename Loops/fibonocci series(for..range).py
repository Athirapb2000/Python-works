n = int(input('Enter the limit: '))
a = 0
b = 1
print(a)
print(b)
for i in range(2, n):
    c = a + b
    print(c)
    a, b = b, c
