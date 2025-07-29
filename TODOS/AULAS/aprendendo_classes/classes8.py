class MeuError(Exception):
    ...

def levantar():
    exception = MeuError("Deu erro")
    raise exception

try:
    levantar()
except MeuError as error:
    print(error)    

