def calculator(func):
    def inner(a, b):
        print('Addition', a+b)
        print('Subtraction', a-b)
        print('Multiplication', a*b)
        print('Division', a/b)
        # return func(a, b)
    return inner

@calculator
def calc(a, b):
    print()
calc(6, 4)
