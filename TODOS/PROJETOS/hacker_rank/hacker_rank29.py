n = int(input())
a = set(map(int, input().split()))

num_operations = int(input())

for _ in range(num_operations):
    operation, _ = input().split()
    other_set = set(map(int, input().strip().split()))
    getattr(a, operation)(other_set)
    
print(sum(a))    