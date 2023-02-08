"""
Polymorphism  - One in many forms
    Types of Polymorphism
        1. Compile time Polymorphism (eg: function overloading or early binding or static binding)
            Python does not have compile time so python does not support compile time polymorphism or overloading
        2. Run time Polymorphism(eg: function overriding or late binding or dynamic binding)
            Function overloading - is one class have more than one function with same function name and different
                                   signatures (number,order and type of parameters)
            Function overriding - different class have different functions with same function name and same signatures
"""

# # compile time polymorphism (function overloading)
# class A:
#     def sum(self, a):
#         print('sum is :', a)
#     def sum(self, a, b):
#         print('sum is :', a+b)
# ob = A()
# ob.sum(10, 20)

# overloading (same class, different number of parameters)
class A:
    def display(self, name=None):
        if name is None:
            print('hello')
        else:
            print('hello '+name)
ob = A()
ob.display()
ob.display('Anu')

# overriding (different class, same method name and signature)
class Rectangle:
    def area(self, l, b):
        print('Area of Rectangle is :', l*b)
class Square(Rectangle):
    def area(self, l, b):
        print('Area of Square is :', l*b)
ob = Square()
ob.area(10, 20)
