n = int(input("Number of students: "))

list_students = []
notas = set()
for student in range(n):
    name = input("enter student name: ")
    notice = float(input("enter student notice: "))
    notas.add(notice)
    list_students.append([name, notice])
notas_ordenadas = sorted(notas)
students_com_notas = []
for student in list_students:
    if notas_ordenadas[1] == student[1]:
        students_com_notas.append(student[0])
        print(student[0])
students_com_notas.sort()

