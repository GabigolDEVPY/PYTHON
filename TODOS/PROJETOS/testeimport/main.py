from files import shared as s
from files.multiplicar_number import multi_number

listas = s.load_lista()

number = int(input("Type a number: "))
result = multi_number(number)
result.sort()

copy_list = result.copy()
copy_list2 = [num + 10 for num in copy_list]

listas = [result, copy_list, copy_list2]

s.save_list(listas)