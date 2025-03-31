

english_students = int(input())
matricules_esnglish = set(map(int, input().split()))

franchise_students = int(input())
matricules_franchise = set(map(int, input().split()))

diference = matricules_esnglish ^ matricules_franchise

print(len(diference))