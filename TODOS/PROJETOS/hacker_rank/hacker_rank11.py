n = int(input())
lista = []
for student in range(n):
    student_lista = input().split()
    nome = ""
    notas = []
    for elemento in student_lista:
        if elemento.isalpha():
            nome += elemento
        elif elemento.isdigit():
            notas.append(int(elemento))
    student = {"name": nome, "notas": notas}
    lista.append(student)

name = input()
for student in lista:
    if student["name"] == name:
        media = sum(student["notas"]) / len(student["notas"])
        print(f"{media:.2f}")