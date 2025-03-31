import matplotlib.pyplot as plt

meses = ["jan", "fev", "mar", "abril", "mai"]
caixa = [1000, 2000, 1400, 1600, 1900]

plt.bar(meses, caixa, color='blue')
plt.axhline(0, color='red', linestyle='--')
plt.title("Fluxo de caixa mensal")
plt.xlabel("Mês")
plt.ylabel("Valor (R$)")

plt.show()