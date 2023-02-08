# OOPs
# class-object
class Employee:
    x = 100
    def display(self):
        print('Simple function')
    def disp():
        print('Without self parameter')

obj = Employee()
obj.display()
print('Value of x is', obj.x)
ob = Employee
ob.disp()

#
class Emp:
    def sum(self, a, b):
        print('sum is', a+b)
    def product(self, a, b):
        print('product is', a * b)

obj = Emp()
obj.sum(30, 40)
obj.product(3, 4)

#
class Sample:
    def read(self, a, b):
        self.x = a
        self.y = b
    def sum(self):
        print('Sum is: ', self.x+self.y)
    def product(self):
        print('Product is: ', self.x * self.y)

obj = Sample()
obj.read(10, 20)
obj.sum()
obj.product()

#
class Sample:
    def read(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        print('Sum is: ', self.a+self.b)
    def product(self):
        print('Product is: ', self.a * self.b)

obj = Sample()
obj.read(20, 20)
obj.sum()
obj.product()

#
class Factorial:
    def fact(self, n):
        f = 1
        for i in range(1, n+1):
            f = f*i
        return f

obj = Factorial()
n = int(input('Enter the number: '))
f = obj.fact(n)
print('Factorial is: ', f)

#
class Facto:
    def fact(sl, x):
        if x==1:
            return 1
        else:
            return x*sl.fact(x-1)

obj = Facto()
n = int(input('Enter the number: '))
f = obj.fact(n)
print('Factorial is: ', f)