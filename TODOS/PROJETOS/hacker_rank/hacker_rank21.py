english_journal = int(input())
list_english = set(map(int, input().split()))

franchise_journal = int(input())
list_franchise = set(map(int, input().split()))

toggeter = list_english.intersection(list_franchise)

print(len(toggeter))
