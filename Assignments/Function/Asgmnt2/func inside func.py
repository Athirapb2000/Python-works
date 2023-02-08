# 1.write a prgm to access a function inside a function
def outer(x):
    def inner(y):
        nonlocal x
        z = x+y
        return z
    return inner
a = outer(5)
print(a(10))
