l = []
def Create():
    num = int(input('Enter the number of elements in the list: '))
    for i in range(num):
        item = int(input('Enter the item: '))
        l.append(item)
    print(l)

def Search():
    item = int(input('Enter the item to be searched: '))
    if item in l:
        print('found')
    else:
        print('not found')

def Remove():
    item = int(input('Enter the item to be removed: '))
    if item in l:
        l.remove(item)
    else:
        print('Item not found in the list')

def Replace():
    old = int(input('Enter the item to be replaced: '))
    new = int(input('Enter new the item replaced: '))
    for i in range(len(l)):
        if l[i] == old:
            l[i] = new
    print(l)

while True:
    opt = int(input('1.Create\n2.Search\n3.Remove\n4.Replace\nEnter your choice: '))
    if opt == 1:
        Create()
    elif opt == 2:
        Search()
    elif opt == 3:
        Remove()
    elif opt == 4:
        Replace()
    else:
        break

Create()
Search()
Remove()
Replace()
