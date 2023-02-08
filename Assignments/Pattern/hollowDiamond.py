n = int(input("enter the number : "))
for i in range(n):
    print("   " * (n-i) + "*", end=" ")
    if i != 0:
        print("   " * (2*i) + "*", end=" ")
    print()
for i in range(n, -1, -1):
    print("   " * (n-i) + "*", end=" ")
    if i != 0:
        print("   " * (2*i) + "*", end=" ")
    print()
