#
print([x for x in 'hello world'])

#
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if 'a' in x]
print(newlist)

#
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

#
prime = [x for x in range(2, 21) if all(x % y != 0 for y in range(2, x))]
print(prime)

# common way
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)

# using list comprehension
h_letters = [letter for letter in 'human']
print(h_letters)

# even or odd
even_no = [x for x in range(101) if x % 2 == 0]
print(even_no)
odd_no = [y for y in range(101) if y % 2 != 0]
print(odd_no)

# sum of n natural no.s
summ = sum([x for x in range(11)])
print(summ)

summ = sum([x for x in range(1, int(input('enter the limit: ')) + 1)])
print(summ)

print([(n*(n+1)/2) for n in range(1, int(input('enter the limit: ')) + 1)])
