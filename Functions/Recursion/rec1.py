# write a prgm to find the sum of natural numbers using recursion
def getsum(num):
    if num == 1:
        return 1
    return num + getsum(num-1)
num = 10
print(getsum(num))

# factorial
def fact(n):                                               # 5*4!........ 5*24=120
    if n == 1:                                             # 4*3!........ 4*6=24
        return 1                                           # 3*2!........ 3*2=6
    else:                                                  # 2*1!........ 2
        return n * fact(n-1)
print('factorial of 5 is:', fact(5))

# sample
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        # print(result)
    else:
        result = 0
    return result
print('Recursion example result')
print(tri_recursion(10))

# fibonacci
def fibo(n):
    if n < 0:
        print('Invalid')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(8))
