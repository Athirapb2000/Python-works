# 1
# 1 2.... pyramid
rows = int(input("Enter the number : "))
for i in range(0, rows+1):
    for j in range(i):
        print(j+1, end=" ")
    print()
print()

# inverted num pyramid
rows = int(input("Enter the number : "))
for i in range(0, rows+1):
    for j in range(rows-i, 0, -1):
        print(j, end=" ")
    print()
print()

# full '*' pyramid
n = int(input("Enter the no.of rows : "))
for i in range(n):
    for s in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()
print()
