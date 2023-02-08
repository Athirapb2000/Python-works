def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

f = fact(int(input('Enter a number : ')))  # or f = fact(1, 2, 3, ..... any number)
print('Factorial is: ', f)
