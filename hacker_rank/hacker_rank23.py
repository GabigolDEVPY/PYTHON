string = input()

print(any(char.isalnum() for char in string))
print(any(char.isalpha() for char in string))
print(any(char.isdigit() for char in string))
print(any(char.islower() for char in string))
print(any(char.isupper() for char in string))