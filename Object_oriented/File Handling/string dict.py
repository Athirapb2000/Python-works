str = 'cat rat mat cat pat rat cat sat cat sat'
print(str)
lst = str.split(' ')
print(lst)
d = {}
for i in lst:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
