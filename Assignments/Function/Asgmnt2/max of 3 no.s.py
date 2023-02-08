# 12.define a function in python that accepts 3 values and returns the maximum of three numbers
def maxm(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(f'{n1} is highest number among 3')
    elif n2 > n1 and n2 > n3:
        print(f'{n2} is highest number among 3')
    else:
        print(f'{n3} is highest number among 3')
maxm(19, 56, 40)
