n = int(input("Number of students: "))

list_students = []

for student in range(n):
    name = input("enter student name: ")
    notice = float(input("enter student notice: "))
    list_students.append([name, notice])