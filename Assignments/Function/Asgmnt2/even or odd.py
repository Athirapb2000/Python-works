# 11.define a function that accepts a number and returns whether the number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')
n = int(input('Enter a number: '))
even_odd(n)
