import mymodule
while True:
    opt = int(input('1.Create\n2.Search\n3.Remove\n4.Replace\nEnter your choice: '))
    if opt == 1:
        mymodule.Create()
    elif opt == 2:
        mymodule.Search()
    elif opt == 3:
        mymodule.Remove()
    elif opt == 4:
        mymodule.Replace()
    else:
        break
