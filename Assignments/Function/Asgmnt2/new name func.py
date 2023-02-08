# 3.Assign a different name to function and call it through the new name.
def employee(name, age):
    print(name, age)
employee('Athira', 22)
new_employee = employee
new_employee('Athira', 22)
