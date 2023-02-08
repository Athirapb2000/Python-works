list1 = [1, 2, 3, 4, 5, 'athira', 'sneha', 7.9]
print(list1)
print(list1[3])
print()

# nested list
my_list = ['welcome', [8, 4, 6], 'Hi']
print(my_list[0][0])
print(my_list[1][1])
my_list.append('archana')
print(my_list)

my_list1 = [1, 2, 3, 4, 'welcome']
my_list1.append('home')
print(my_list1)

my_list1.remove('home')
print(my_list1)

my_list1.insert(2, [0, 1, 2, 3])
my_list1.insert(3, 'John')
print(my_list1)

mylist3 = ['hello']
mylist3.extend(my_list1)
print(mylist3)

name = 'Python'

print(name[:])
print(name[0:])
print(name[::-1])
print(name[::-2])
print(name[::2])
print(name[0]+name[1])
print(name[-1:-3:-1])

list1 = [1, 2, 3]
list1.pop(2)
print(list1)
list1.pop()
print(list1)

list2 = [1, 2, 3]
print(list2.clear())

list3 = [[1, 2, 3], 'hi', 'hello', [6, 7]]
print(list3.index('hello'))

list4 = [1, 2, 3, 1, 1]
print(list4.count(1))

list5 = [1, 3, 2, 5, 9, 6]
list5.sort()
print(list5)

list6 = [1, 2, 3, 8, 5]
list6.reverse()
print(list6)

list7 = [1, 2, 3]
print(list7.copy())

list8 = ['a', ['bb', 'cc'], 'd']
list8[1].insert(0, 'ss')
print(list8)
