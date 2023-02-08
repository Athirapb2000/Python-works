listofdict = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print('The given dictionary is : ', listofdict)
newdict = {}
list1 = []
for d in listofdict:
    # print(d)
    p = list(d.values())
    list1.append(p[0])
    # print(list1)
    list1.append(p[1])
    # print(list1)
# print(list1)
for i in range(0, len(list1), 2):
    # print(i)
    if list1[i] in newdict:
        rep = list1[i]
        index = list1.index(rep)
        list1[index+1] = list1[index+1]+list1[i+1]
        newdict[list1[i]] = list1[index+1]
    else:
        newdict.setdefault(list1[i], list1[i+1])
print('The combined dictionary is : ', newdict)
