import random

lista = {
        "eu":["vou", "gosto", "jantei", "não", "dormirei"],       
        "vou":["jogar", "viajar", "jantar", "treinar", "fazer", "dormir"],       
        "gosto":["dela", "de", "mais", "sempre", "talvez"],     
        "jantei":["hoje", "cedo", "semana passada", "salada", "carne"],       
        "não":["vou", "sei", "gosto mais", "vou", "jantarei"],           
        "dormirei":["hoje", "cedo", "depois", "talvez"],      
    }


for i in range(1000):
    def fazer_frase():
        first = random.choice(lista["eu"])
        second = random.choice(lista[first])
        frase = (f"eu {first} {second}")
        print(frase)
    fazer_frase()
    