from load import save_file, load_list_scores_lifes

def loja():
    while True:
        data = load_list_scores_lifes
        option = int(input(
            "1 LIFE = 10000"
            "2 LIFE = 20000"
            "3 LIFE = 30000"
            "4 LIFE = 40000"
            "5 LIFE = 50000"
            "6 LIFE = 60000"
        ))
        if len(option) >1:
            print("Type just one digit")
        valid = "1,2,3,4,5,6"

        if option not in valid:
            print('Option invalid, type try')

        data["lifes"] += option    
    
    