num = int(input("Enter the levels you want : "))
n = num // 2
for i in range(2, n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    if num % 2 == 0:
        for j in range(2*(n-i-1)):
            print(" ", end="")
    for j in range(2*(n-i-1)+1):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()
# lower part
for i in range(num, 0, -1):
    for j in range(num-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print("* ", end="")
    print()

