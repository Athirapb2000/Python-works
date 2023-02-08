"""
1.write a program to get a string from a given string where all the occurrences of its first char have been changed to
  '$',except the first char itself.
  sample i/p: restart
  o/p: resta$t
"""
str1 = 'restart'
str2 = str1[0]
# str1 = str1.lower()
for i in range(1, len(str1)):
    if str1[i] == str1[0]:
        str2 = str2 + '$'
        # print(str2)
    else:
        str2 = str2 + str1[i]
        # print(str2)
print(str2)

# OR
str1 = 'retrieve'
char = str1[0]
length = len(str1)
str2 = str1.replace(char, '$')
str3 = char + str2[1:]
print(str3)

"""
2.WAP for python function that takes a list of words and returns the length of the longest one.
"""
lst = list(input('Enter space seperated words: ').split())
m = max(lst)
print(f'length of the longest word {m} is {len(m)}')
