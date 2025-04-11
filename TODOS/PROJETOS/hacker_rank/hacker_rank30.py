def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    lines = []
    for i in range(size):
        left = alphabet[size-1:i:-1]  
        right = alphabet[i:size]     
        line = '-'.join(left + right)  
        lines.append(line.center(4*size-3, '-'))  

    for line in lines[::-1] + lines[1:]:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


