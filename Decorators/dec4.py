def upper_decor(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper()

def hello_name():
    return 'hello'
f = upper_decor(hello_name)
print(f)

# OR
def upper_decor(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

@upper_decor
def hello_name(name):
    return 'hello' + name
print(hello_name(' Athira'))
