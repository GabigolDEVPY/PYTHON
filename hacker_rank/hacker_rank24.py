def count_substring(string, sub_string):
    cont = 0
    vezes = 0
    for char in string:
        if string[cont: cont + len(sub_string)] == sub_string:
            vezes += 1
        cont +=1
    return vezes    

    
string = input().strip()
substring = input().strip()

count = count_substring(string, substring)

print(count)