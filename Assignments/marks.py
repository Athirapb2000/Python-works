print("Enter the Marks in Out of 100")
mark1 = int(input("Enter the marks in Physics: "))
mark2 = int(input("Enter the marks in Chemistry: "))
mark3 = int(input("Enter the marks in biology: "))
mark4 = int(input("Enter the marks in Mathematics: "))
mark5 = int(input("Enter the marks in Computer: "))
per = ((mark1+mark2+mark3+mark4+mark5)/500)*100
print("Percentage:", per, "%")

if per >= 90:
    print("Grade: A")
elif per >= 80:
    print("Grade: B")
elif per >= 70:
    print("Grade: C")
elif per >= 60:
    print("Grade: D")
elif per >= 50:
    print("Grade: E")
else:
    print("Grade: F")
