"""
CONSTRUCTOR
    constructors are the member functions of a class which will automatically executed when a object of a class is
    created. Constructors do not have return value. We can define a constructor by using __init__(self)
    Mainly 2 types of constructors
    1. Non Parameterized Constructor (Default Constructor)
    2. Parameterized Constructor
"""

# Non parameterized constructor
class A:
    def __init__(self):
        print('Non parameterized constructor')
ob = A()

# Parameterized constructor
class A:
    def __init__(self, name):
        print('Parameterized constructor')
        self.na = name
    def display(self):
        print('Name is :', self.na)
ob = A('Athira')
ob.display()

# destructor
class A:
    def __init__(self, name):
        print('Parameterized constructor')
        self.na = name
    def __del__(self):
        print('destructors')
    def display(self):
        print('Name is :', self.na)
obj = A('Athira')
# del obj
obj.display()
