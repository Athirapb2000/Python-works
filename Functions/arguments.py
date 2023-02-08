# Arguments/positional args
def my_function(msg1, msg2):
    print(msg1 + " " + msg2)
my_function(' How are you\n', 'Hi dears')

# Arbitrary args
def my_func(*names):
    print('Hi', names)
my_func('Athira')
my_func('Aparna')
my_func('Sneha')

# Keyword args
def myfunc(name1, name2, name3):
    print('last name is ' + name2)
myfunc('Athira', name2='Baby', name3='baby')

# arbitrary keyword args
def myfunc(**name):
    print('The last name is ' + name['lname'])
myfunc(fname='Athira', lname='Baby')

# Default value
def func(country='Norway'):
    print('I am from ' + country)
func('Sweden')
func('India')
func()
func('Brazil')
