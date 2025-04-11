n = int(input())

list_students = []
notas = set()
for student in range(n):
    name = input()
    notice = float(input())
    notas.add(notice)
    list_students.append([name, notice])
notas_ordenadas = sorted(notas)
students_com_notas = []
for student in list_students:
    if notas_ordenadas[1] == student[1] and len(notas_ordenadas) > 1:
        students_com_notas.append(student[0])
students_com_notas.sort()
for student in students_com_notas:
    print(student)

