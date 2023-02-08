s1 = input('Enter the first string : ')
s2 = input('Enter the second string : ')
s1 = s1.lower()
# print(s1)
s2 = s2.lower()
# print(s2)
if len(s1) == len(s2):
    str1 = sorted(s1)
    # print(str1)
    str2 = sorted(s2)
    # print(str2)
    if str1 == str2:
        print(s1, 'and', s2, 'are anagram')
    else:
        print(s1, 'and', s2, 'are not anagram')
else:
    print(s1, 'and', s2, 'are not anagram')
