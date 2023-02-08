# super class
class A:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public data member function
    def displayPublicMembers(self):
        # accessing public data members
        print('Public Data Member: ', self.var1)

    # protected member function
    def _displayProtectedMembers(self):
        # accessing private data members
        print('Protected Data Member: ', self._var2)

    # private member function
    def __displayPrivateMembers(self):
        # accessing private data members
        print('Private Data Member: ', self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accessing private member function
        self.__displayPrivateMembers()

# derived class
class B(A):

    # constructor
    def __init__(self, var1, var2, var3):
        A.__init__(self, var1, var2, var3)

    # public member function
    def accessProtectedMembers(self):
        # accessing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of the derived class
obj = B('Pub_Red', 'Pro_White', 'Private_Green')

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# object can access public member
print('Object is accessing public member:', obj.var1)
# object can access protected member
print('Object is accessing protected member:', obj._var2)

# object cannot access private member, so it will generate Attribute error
print(obj._A__var3)  # Accessing name mangled variables

"""
Name Mangling
A process in which any given identifier with one trailing underscore and two leading underscores is textually with the 
_ClassName__identifier is known as Name mangling.
In _ClassName__identifier name,ClassName is the name of current class where identifier is present.
"""