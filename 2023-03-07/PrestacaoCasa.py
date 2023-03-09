import math
import random
import time

def generate_numbers():
    list = []
    x = int(time.time()) / (2**31)
    list.append(x)
    for i in range(1,30):
        x = (1103515245*x+12345) % (2**31)
        list.append(x / (2**31))
    return list

maturidade = 30
capital_divida = 100000
spread = 2
euribor = 3

lista_numeros_aleatorios = generate_numbers()
z1, z2 = box_muller(u1, u2)

print("ano, capital divida, juro_capital, amortizacao, prestacao")
for ano in range(1, 30):

    juro = (spread + z1) / 100

    prestacao = capital_divida * ((1-(1/(1+juro)))/((1/(1+juro))-(1/(1+juro))**31))
    
    juro_capital = (capital_divida - (prestacao*ano)) * juro
    amortizacao = prestacao - juro_capital

    print(str(ano) + ", " + str(capital_divida) + "," + str(juro_capital) + "," + str(amortizacao) + "," + str(prestacao))    
    
    capital_divida = capital_divida - amortizacao