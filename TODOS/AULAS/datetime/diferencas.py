from datetime import datetime

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime("11/05/2005 9:00:00", fmt)
# date_fim = datetime.strptime("18/08/2025 9:00:00", fmt)
date_fim = datetime.now()
delta = data_inicio - date_fim
print(delta)