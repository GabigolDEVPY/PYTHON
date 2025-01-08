if __name__ == '__main__':
    list = []
    N = int(input())
    for iter in range(N):
        comand_num_position = input().split()
        if "insert" in comand_num_position:
            position = int(comand_num_position[1])
            number = comand_num_position[2]
            if list == []:
                list.append(number)
                continue
            list[position] = number
    print(list)


