"""
pyramid of horizontal number tables
"""
rows = int(input('Enter the number of rows: '))
for i in range(1, rows+1):       # rows
    for j in range(1, i+1):      # columns
        print(i * j, end=' ')
    print()
