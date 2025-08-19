from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

def calcular_tempo():
    parcelas = 60
    valor = float(10000000)
    valor_parcelas = float(valor / parcelas)
    data_inicial = datetime.now().date()
    juros = 0

    for parcela in range(parcelas):
        nova_data = data_inicial + relativedelta(months=parcela)
        juros += parcela // 0.03
        # print(f"{nova_data} VALOR R$: {valor_parcelas:.2f}")
    # print(f"JUROS FINAL R$: {juros}")    

calcular_tempo()

print(calendar.monthrange(2025, 8))
print(calendar.weekday(2025, 8, 10))
# print(list(enumerate(calendar.day_name)))
print(calendar.monthcalendar(2025, 8))
print(calendar.calendar(2025))