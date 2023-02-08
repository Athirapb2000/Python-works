"""
Inheritance   - to acquire the properties of one to another class (use-Code Reusability)
    Types of Inheritance
        1. Single Inheritance      - One Base class and one derived class
        2. Multilevel Inheritance  - One base class, intermediatory class and base class
        3. Multiple Inheritance    - Multiple(or two) base class and one derived class
        4. Hierarchical Inheritance- One base class and multiple derived classes
        5. Hybrid Inheritance      - Combination of Hierarchical and multiple
"""

# single inheritance
class A:
    def displayA(self):
        print('Base class method')
class B(A):
    def displayB(self):
        print('Derive class method')
ob = B()
ob.displayA()
ob.displayB()

#
class A:
    def read(self):
        self.x = int(input('Enter a number: '))
        self.y = int(input('Enter a number: '))
class B(A):
    def sum(self):
        print('Sum is: ', self.x+self.y)
obj = B()
obj.read()
obj.sum()

# Multilevel Inheritance
class A:
    def read(self):
        self.x = int(input('Enter a number : '))
        self.y = int(input('Enter a number : '))
class B(A):
    def sum(self):
        self.s = self.x+self.y
        print('Sum is :', self.s)
class C(B):
    def avg(self):
        print('Average is :', self.s/2)
obj = C()
obj.read()
obj.sum()
obj.avg()

# Hierarchical Inheritance
# A-read B-sum C-avg D-product
class A:
    def read(self):
        self.x = int(input('Enter a number : '))
        self.y = int(input('Enter a number : '))
class B(A):
    def sum(self):
        print('Sum is :', self.x+self.y)
class C(A):
    def avg(self):
        print('Average is :', (self.x+self.y)/2)
class D(A):
    def product(self):
        print('Product is :', self.x*self.y)

ob1 = B()
ob1.read()
ob1.sum()

ob2 = C()
ob2.read()
ob2.avg()

ob3 = D()
ob3.read()
ob3.product()

# Multiple Inheritance
# A-name,age,address...B-salary.....c-A,B
class A:
    def employee(self):
        self.name = input('Enter your name : ')
        self.age = int(input('Enter your age : '))
        self.address = input('Enter your address : ')
class B:
    def salary(self):
        self.salary1 = int(input('Enter your salary : '))
class C(A, B):
    def display(self):
        print(self.name)
        print(self.age)
        print(self.address)
        print(self.salary1)
obj = C()
obj.employee()
obj.salary()
obj.display()
