from scipy.optimize import newton


fluxos = [-1000, 200, 300, 400, 500, 600]

def calcular_vpl(taxa):
    return sum(valor / (1 + taxa) ** i for i, valor in enumerate(fluxos))


tir = newton(calcular_vpl, x0=0.1)  


print(f"Taxa Interna de Retorno (TIR): {tir * 100:.2f}%")
