if __name__ == '__main__':
    list = []
    N = int(input())
    for iter in range(N):
        comand_num_position = input().split()
        if "insert" in comand_num_position:
            position = int(comand_num_position[1]) 
            number = comand_num_position[2]
            if list == [] or len(list) < position:
                list.append(int(number))
                continue
            list.insert(position, int(number))
        elif "append" in comand_num_position:
            list.append(int(comand_num_position[1]))
            
        elif "print" in comand_num_position:
            print(list)
        elif "remove" in comand_num_position:
            list.remove(int(comand_num_position[1]))
        elif "sort" in comand_num_position:
            list.sort() 
        elif "pop" in comand_num_position:
            list.pop()
        elif "reverse" in comand_num_position:
            list.reverse()
