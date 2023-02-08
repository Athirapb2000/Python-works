#
name = 'Athira'
for i in name:
    print(i)
print()

#
for i in range(0, 11):
    print(i)
print()

#
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5
for i in list1:
    c = n*i
    print(c)
print()

#
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in list1:
    sum = sum + i
print('The sum is :', sum)
print()

#
sum = 0
for i in range(1, 11):
    sum = sum+i
print('The sum is :', sum)
print()

# even no.s
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
print()

# even no.s
for i in range(2, 11, 2):
    print(i)
print()

# odd no.s
for i in range(1, 11, 2):
    print(i)
print()

#
n = int(input('Enter the number : '))
for i in range(1,n):
    n = n+i
print(n)

# multiplication table
n = int(input('Enter the number : '))
for i in range(1, 11):
    c = n*i
    print(i, '*', n, '=', c)
print()
