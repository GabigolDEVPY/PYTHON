def check_subsets():

    t = int(input())
    
    results = []
    
    for _ in range(t):

        n_a = int(input())  
        set_a = set(map(int, input().split()))  
        
        n_b = int(input())  
        set_b = set(map(int, input().split()))  
        
        results.append(set_a.issubset(set_b))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    check_subsets()