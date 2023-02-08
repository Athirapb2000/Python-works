choice = input("enter the choice +,-,*,/ : ")
a = int(input("enter the 1st num: "))
b = int(input("enter the 2nd num: "))
if choice=='+':
    print("sum is", a+b)
elif choice=='-':
    print("difference is", a-b)
elif choice=='*':
    print("multiplication is", a*b)
elif choice=='/':
    print("division is", a/b)
else:
    print("invalid")