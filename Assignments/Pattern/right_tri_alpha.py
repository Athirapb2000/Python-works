n = int(input("Enter the levels you want : "))
k = 1
ch = chr(64+k)
for i in range(n+1):
    for j in range(i):
        print(ch, end=' ')
        k = k+1
        ch = chr(64+k)
    print()
