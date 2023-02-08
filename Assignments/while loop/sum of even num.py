max = int(input("Enter the maximum value : "))
total = 0
num = 1
while num <= max:
    if num % 2 == 0:
        print(num)
        total = total + num
    num = num + 1
print("Sum of even numbers from 2 to", max, "is :", total)
