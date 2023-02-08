num = int(input("enter the number : "))
print()
half = round(num/2)

for i in range(2, half):
    print(" "*(half-i-1)+"*"*(2*i+1)+"  "*(half-i)+"*"*(2*i+1))
for i in range(num, 0, -1):
    print(" "*(num-i)+"*"*(2*i-1))
