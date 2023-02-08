rows = int(input("Enter the number : "))
print()
for i in range(rows+1, 0, -1):
    for j in range(i-1, 0, -1):
        print(j, end='  ')
    print()
