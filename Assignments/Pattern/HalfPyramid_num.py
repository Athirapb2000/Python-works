rows = int(input("Enter the number : "))
for i in range(0, rows+1):
    for j in range(i):
        print(j+1, end=" ")
    print()
