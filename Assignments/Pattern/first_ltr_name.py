n = ""
for i in range(0, 7):  # row
    for j in range(0, 7):  # column
        if(((j == 1 or j == 5) and i != 0) or ((i == 0 or i == 3) and (j > 1 and j < 5))):
            n = n + '*'
        else:
            n = n + " "
    n = n + '\n'
print(n)
