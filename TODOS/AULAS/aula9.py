velocidade = int(input('Digite a velocidade do carro: '))

if velocidade <= 80:
    print('você foi multado em 10 reais')
elif velocidade <= 90:
    print('você foi multado em 20 reais')
elif velocidade <= 100:
    print('você foi multado em 30 ')    
else:
    print('sua multa é incalculavel')    
