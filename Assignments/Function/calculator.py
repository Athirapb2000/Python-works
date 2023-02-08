def add(a, b):
    print('sum is: ', a+b)
def sub(a, b):
    print('difference is: ', a-b)
def mul(a, b):
    print('product is: ', a+b)
def div(a, b):
    print('quotient is: ', a/b)
num1 = int(input('Enter first number: '))
num2 = int(input('Enter Second number: '))
op = int(input('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division'
               '\nPlease select your option'))
if op == 1:
    add(num1, num2)
elif op == 2:
    sub(num1, num2)
elif op == 3:
    mul(num1, num2)
elif op == 4:
    div(num1, num2)
else:
    print('Please enter a valid option: ')
