# 2.write a python function to create and print a list where the values are square of numbers between 1 and 30
def val():
    list1 = []
    for i in range(1, 30):
        list1.append(i**2)
    print(list1)
val()
