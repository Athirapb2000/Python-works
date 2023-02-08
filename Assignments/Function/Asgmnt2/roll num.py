# 9.define a function that accepts roll number and returns whether the student is present or not
def student(rollnum):
    rnum = [1, 2, 3, 4, 5]
    if rollnum in rnum:
        print('roll number', rnum, 'is present')
    else:
        print('roll number', rnum, 'is  not present')
rollnum = int(input('Enter roll number'))
student(rollnum)
