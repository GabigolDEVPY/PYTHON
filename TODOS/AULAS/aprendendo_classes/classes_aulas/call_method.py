class Callme():
    def __init__(self, phone):
        self.phone = phone
        
    def __call__(self,nome, *args, **kwds):
        print(nome, "está chamando", self.phone)
        args = args
        print(args)
        if "casa" in args:
            print("tem casa")
        return 1234
        
        
call1 = Callme('1231312')
retorno = call1("Gabriel", "casa", "carro", "animal")
print(retorno)