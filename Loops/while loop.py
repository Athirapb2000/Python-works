#
i = 1
while i <= 10:
    print(i)
    i = i+1
print()

#
i = 1
number = int(input('Enter the num : '))
while i <= 10:
    print('%d X %d = %d' % (i, number, number*i))
    i = i+1
print()

# sum of n natural no.s
n = int(input('Enter the num : '))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print('The sum is:', sum)
