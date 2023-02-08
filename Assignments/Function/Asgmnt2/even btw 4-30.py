# 4.generate a python list of all the even numbers between 4 and 30
def even(a, b):
    n = []
    for i in range(a, b, 2):
        n.append(i)
    return n
print(even(4, 30))
