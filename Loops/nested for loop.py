# '*' pyramid
rows = int(input('Enter the no.of rows : '))
for i in range(0, rows+1):
    for j in range(i):
        print('*', end=" ")
    print()
print()

# inverted '*' pyramid
rows = int(input("Enter the no.of rows : "))
for i in range(rows):
    for j in range(rows-i):
        print('*', end=" ")
    print()

# 1
# 1 2.... pyramid
rows = int(input("Enter the number : "))
for i in range(0, rows+1):
    for j in range(i):
        print(j+1, end=" ")
    print()
