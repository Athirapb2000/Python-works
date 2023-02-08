# datatypes in python
"""
1. number
        immutable
2. string
        immutable
3. list
        mutable
4. tuple
        immutable
5. dictionary
        mutable
6. set
        immutable
"""
# number
x = 4
print(x)
print(type(x))

# string  # immutable
name = "athira"
age = "22"
print(type(name))
print(type(age))

# list
list1 = [1, 2, 3, 4, 5, 6, 6]
print(list1)
print(type(list1))

# dictionary
dict1 = {"name": "athira"}
print(dict1)
print(type(dict1))

# set
a = {1, 2, 3}
print(a)
print(type(a))

# tuple
a = "athira", "sneha", "aparna"
print(a)
print(type(a))

# string indexing
str2 = "hello world"
print(str2[0])
print(str2[-1])

# string slicing
print(str2[0:2])
print(str2[0:-1])
print(str2[2:5])
print(str2[-4:-1])
print(str2[7:10])
print(str2[::-1])  # reverse order
print(str2[::-2])  # alternatives wl be print
print(str2[::-4])
print(str2[0:-1])
print(str2[-2:-6:-1])
print(str2[-11:-6])

# string upper lower etc..
print(str2.lower())
print(str2.upper())
str3 = "AtHirA"
print(str3.swapcase())
print(str2.capitalize())
print(str2.title())

print(str2.isupper())
print(str2.islower())
print(str2.isalpha())
