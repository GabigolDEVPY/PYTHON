import db as db

class Vagas():
    @staticmethod
    def listar_lugares():
        return db.execute_comand("SELECT * FROM vagas")
    
    def marcar_lugar(dados):
        result = db.execute_comand("UPDATE vagas SET nome = %s, agendada = True WHERE vaga = %s AND agendada = FALSE ", dados["nome"], dados["vaga"])
        if result is None:
            return 0
        return 
    
    def desmarcar_lugar(dados):
        dados = dados
        result = db.execute_comand("UPDATE vagas SET agendada = False, nome = 'vazio' WHERE vaga = %s AND nome = %s", dados["vaga"], dados['nome'])
        