def average(arr):
    list = set(arr)
    result = sum(list) / len(list)
    return result




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)