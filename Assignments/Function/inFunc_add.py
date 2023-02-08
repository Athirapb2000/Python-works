def outer(a, b):
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5
result = outer(5, 10)
print(result)

# or
def calc(a, b):
    def addition():
        c = a + b
        return c
    return addition()+5
print(calc(4, 6))
