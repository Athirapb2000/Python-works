#
str1 = "Hello"
str2 = 4
new_str = str1 + ' ' + str(str2)
print(new_str)

#
str3 = "Hi"
str4 = "Athira"
new_str = str3 + ' ' + str4
print(new_str)

print(len(new_str))

# looping through strings  # while loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# for loop
fruit = 'banana'
for i in fruit:
    print(i)

# for
fruit = 'apple'
for letter in 'apple':
    print(letter)

# find

a = fruit.find('e')
print(a)

# replace
greet = 'Hello Sneha'
a = greet.replace('Sneha', 'Athira')
print(a)
b = greet.replace('e', 'o')
print(b)
c = greet[2].replace('e', 'o')
print(c)
