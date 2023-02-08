s1 = input('Enter the string : ')
f = {}
for i in s1:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
print('Character\tfrequency')
for i, frequency in f.items():
    print(i, '\t\t\t', frequency)
