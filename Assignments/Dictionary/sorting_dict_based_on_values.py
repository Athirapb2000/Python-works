dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("The given dictionary is : ", dict1, "\n")
val = list(dict1.items())                         # Creates a list of tuples of key:value pairs
newval = []
newvalf = []

for i in val:                                     # key:value pair
    irev = i[::-1]                                # ordering value:key format
    newval.append(irev)                           # appending value:key pairs to empty list
# print(newval)
val.clear()                                       # clearing key:value pair list
newval.sort()
print(newval)                                     # sorting based on values  value:key

for i in newval:
    irevf = i[::-1]                               # reversing whole value:key list back to key:value
    val.append(irevf)                             # appending to list
# print(val,"/n")

for i in (newval[::-1]):                          # taking reverse of value:key list for taking descending order
    i = i[::-1]                                   # reversing back to key:value format
    newvalf.append(i)                             # appending descending order pairs to list
# print(newvalf,"/n")

print("The dictionary in ascending order of key values is : ", dict(val), "\n")
print("The dictionary in descending order of key values is : ", dict(newvalf))
