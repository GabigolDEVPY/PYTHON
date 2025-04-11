
def door_mat(N, M):
    for i in range(1, N, 2): 
        pattern = (".|." * i).center(M, "-")
        print(pattern)


    print("WELCOME".center(M, "-"))


    for i in range(N-2, 0, -2):
        pattern = (".|." * i).center(M, "-")
        print(pattern)

if __name__ == "__main__":
    N, M = map(int, input().split())
    door_mat(N, M)

    