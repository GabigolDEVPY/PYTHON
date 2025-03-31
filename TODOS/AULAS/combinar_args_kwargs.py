def combinar_tudo(*args, **kwargs): # empacota os argumentos que receber
    print("Args:", args)
    print("Kwargs:", kwargs)
    
combinar_tudo(1, 2, 3, nome="Gabigordo", altura=1.79,)