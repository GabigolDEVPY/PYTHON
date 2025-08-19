import os 
import json

class Manipulate:
    def __init__(self):
        self.pasta_dir = os.path.join(os.path.expanduser("~"), "Documents", "SaveJson")
        self.arquivo = os.path.join(self.pasta_dir, "arquivo_json.json" )
        os.makedirs(self.pasta_dir, exist_ok=True)
        
    def save_file(self, arquivo=None):
        with open(self.arquivo, "w", encoding="UTF-8") as file:
            if arquivo is None:
                arquivo = []
            return json.dump(arquivo, file, ensure_ascii=False, indent=4)
                
    def load_file(self):
        with open(self.arquivo, "r") as file:
            return json.load(file)
            
people = {
    "Nome": "Gabriel",
    "Idade": 18
}

fileee = Manipulate()
fileee.save_file(people)
print(fileee.load_file())


