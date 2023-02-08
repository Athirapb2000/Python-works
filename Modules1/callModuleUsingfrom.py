from mymodule import *
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
