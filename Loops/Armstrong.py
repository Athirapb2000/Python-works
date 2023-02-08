num = int(input("Enter the number: "))
sum = 0
i = num
while i > 0:
    n = i % 10
    sum += n * n * n
    i //= 10
if num == sum:
    print(num, 'is armstrong number')
else:
    print(num, 'is not armstrong number')
