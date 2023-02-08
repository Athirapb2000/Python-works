def sample():
    print('Hello Athira')
sample()

# Example 1
def sum():
    a = 10
    b = 20
    c = a + b
    return c
print('The sum is', sum())

# eg2
def sample(name):
    print('Hi dears, my name is', name)
sample('Athira')

# eg3
def func(*names):
    print('My name is', names)
func('Athira', 'Aparna', 'Sneha')

# eg4
def mulfunc(child1, child2, child3):
    print('The youngest child is ' + child3)
mulfunc(child1='Athira', child2='Aparna', child3='Sneha')

