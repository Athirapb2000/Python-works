num = int(input("Enter the number : "))
count = 0
i = 2
while i < num:
    if num % i == 0:
        count = 1
        print(num, "is not a prime number")
    i = i + 1
if count == 0:
    print(num, "is a prime number")
