# i/p : 1234abcd
# o/p : dcba4321
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s = '1234abcd'
print('The string is: ', s)
print('Reverse of the string is: ', reverse(s))

