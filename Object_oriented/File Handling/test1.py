f = open('test1', 'r')
# for i in f:
#     print(i)
# f.close()

# print(f.read())

# print(f.read(8))

# print(f.readline())
# print(f.readline())

# f = open('test1', 'a')
# f.write('python is a oop')
# f.close()

# print(f.read())

# for i in f:
#     print(i)
# f.close()

# f = open('test1', 'w')
# f.write('python is a oop')
# f.close()
#
# f = open('test1', 'r')
# for i in f:
#     print(i)
# f.close()

'''seek() - it returns a new position - file.seek(offset)'''

# f.seek(8)
# print(f.readline())
# f.close()

'''tell()- it returns the current position of the file- fileobject.tell()'''
f.readline()
pos = f.tell()
f.close()
print('position is:', pos)

