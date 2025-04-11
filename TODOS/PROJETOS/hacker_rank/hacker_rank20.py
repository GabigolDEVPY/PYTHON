english_journal = int(input())
list_english = set(map(int, input().split()))
franchise_journal = int(input())
list_franchise = set(map(int, input().split()))


toggetter = list_english.union(list_franchise)
print(len(toggetter))
