def listMul(list1):
    p = 1
    for i in list1:
        p = p * i
    return p
list1 = [1, 2, 3, 4]
print(list1)
print('product: ', listMul(list1))
