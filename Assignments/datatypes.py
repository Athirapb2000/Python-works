# 1.remove empty strings from a list strings
str1 = ['john', '', 'jack', 'emma', '', 'jins', 'lina']
i = 0
while i < len(str1):
    if len(str1[i]) == 0:
        str1.pop(i)
    i = i + 1
print(str1)

# 2.remove all the repeating letters from each word
# i/p: Let's google the pineapple
# o/p: Let's gole the pineal
str1 = "Let's google the pineapple"
str2 = str1.split(' ')
str3 = []
for i in str2:
    l = ""
    for j in i:
        if j in l:
            continue
        else:
            l = l + j
    str3.append(l)
print(' '.join(str3))



# 3.replace each special symbol with # in the following string
str1 = '/*jon is @developer & musician!!'
str1 = str1.replace('/', '#').replace('*', '#').replace('@', '#').replace('&', '#').replace('!', '#')
print(str1)

# 4.reverse a list in python
list1 = [100, 200, 300, 400, 500]
print(list1[::-1])

# 5.extend nested list by adding the sublist
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
for i in sub_list:
    list1[2][1][2].append(i)
print(list1)
