dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("The given dictionary is : ", dict1, "\n")
asDict = {}
disDict = {}
val = list(dict1.values())
val1 = list(dict1.values())
val.sort()                                       # sorted values in ascending order
val1.sort(reverse=True)                          # sorted values in descending order
key = list(dict1.keys())
for i in val:
    index = list(dict1.values()).index(i)
    asDict[key[index]] = i
for i in val1:
    index = list(dict1.values()).index(i)
    disDict[key[index]] = i
print("Ascending Dictionary", asDict.items(), "\n Descending Dictionary", disDict)
