def calculate_profit(billing, profit):
    total = 0
    total = (billing / 100) * profit
    print(f"Revenue was R${billing:.2f} reais\n"
        f"The profit was R$ {total:.2f} reais")
    
billing  = int(input("report billing: "))
profit  = int(input("report profit: "))

calculate_profit(billing, profit)    