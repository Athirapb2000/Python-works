f = open('test2', 'r')
dic = {}
for i in f:
    var = i.split(' ')
    for j in var:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j] += 1
print(dic)
