def inner(x, y):
    sum = x + y
    print(sum)
    def outer(z):
        return z + a
    p = outer(sum)
    print(p)
d = int(input('d: '))
e = int(input('e: '))
a = int(input('a: '))
inner(d, e)
