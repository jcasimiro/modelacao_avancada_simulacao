#!/usr/bin/env python
# coding: utf-8

# In[15]:



import time
import numpy as np
import pandas as pd

#usar o  linear congruent method (LCM) para gerar numeros aleatorios entre 0 e 1
xzero = int(time.time())
print(xzero)
aa = 110351525
cc = 12345
modulo = pow(2,31)

#numero de anos do emprestimo
nyears = 30
#Para O Gerador Aleatório Box Muller Vamos necessitar de 1 par de 15 numeros

npares=nyears//2
print(npares)

#expressao para calcular o Xis: Xn=(aa*X[n-1]+cc) mod (2^31), recorrendo ao método LCM

Xis = np.zeros(npares)
Xis[0] = (aa *xzero + cc) % (modulo)

for i in range(1,npares):
    Xis[i] = (aa * Xis[i-1] + cc) % (modulo)

# como pretendemos que X seja uma uniforme com valores entre 0 e 1 , vamos dividir o Array de dos valores
# obtidos por 2^31:

Xn=Xis/modulo
print(Xn)

#Agora vamos recorrer ao método Box Muller para calcular as gaussianas para serem usadas como taxas de juro, com media de 3% e desvio padrao de 1%
    
#primeiro criar os respetivos arrays de 15  numeros a zero
G1=np.zeros(npares)
G2=np.zeros(npares)

G1[0]=np.sqrt(-2 * np.log(Xn[0])) * np.cos(2 * np.pi * Xn[0])
print(G1)
 
G2[0]=np.sqrt(-2 * np.log(Xn[0])) * np.sin(2 * np.pi * Xn[0])
print(G2)

for i in range(1,npares):
    G1[i]=(np.sqrt(-2 * np.log(Xn[i])) * np.cos(2 * np.pi * Xn[i]))
    G2[i]=(np.sqrt(-2 * np.log(Xn[i])) * np.sin(2 * np.pi * Xn[i]))
print(G1)   
print(G2)

#como se pretendem 30 valores de taxas, com valores positivos, vamos unir os pares:

GP= np.concatenate((np.abs(G1),np.abs(G2)), axis=None) 
print(GP)


# definir a media e desvio padrão pretendidos
media = 0.03
desvio_padrao = 0.01

#Calcular o valor das taxas de Juro com base nas gaussianas obtidas, média e desvio padrão pretendidos

Tx= media + GP * desvio_padrao
print("Taxas de Juro:",Tx)

mean = np.mean(Tx)
std = np.std(Tx)
print("Média:", mean)
print("Desvio padrão:", std)


######              SIMULAÇÃO DO EMPRESTIMO BANCARIO          #####
# Agora que temos os valores gerados para as taxas de juro, vamos simular as condiçoes de um emprestimo 
# de 100000€ a 30 anos, com spread de 2%

#condiçoes do empréstimo:
    

valor_emprestimo = 100000  # €
prazo = 30  # anos
spread = 0.02  # 2%
divida =np.zeros(nyears)
juro_total=np.zeros(nyears)
prestacao_anual=np.zeros(nyears)
juro_capital_em_divida =np.zeros(nyears)
amortizacao=np.zeros(nyears)
anos_em_falta=np.zeros(nyears)
coltab = []

# ano zero dp emprestimo
divida[0]=valor_emprestimo
anos_em_falta[0]=nyears
juro_total[0]=Tx[0]+spread
prestacao_anual[0]=divida[0]*((1-(1/(1+juro_total[0])))/((1/(1+juro_total[0]))-(1/(1+juro_total[0]))**(anos_em_falta[0]+1)))
juro_capital_em_divida[0]=juro_total[0]*divida[0]
amortizacao[0]=prestacao_anual[0]-juro_capital_em_divida[0]

coltab.append([divida[0], juro_total[0],prestacao_anual[0],juro_capital_em_divida[0],amortizacao[0]])

for i in range(1,nyears):
    anos_em_falta[i]=anos_em_falta[i-1]-1
    divida[i]=divida[i-1]-amortizacao[i-1]
    juro_total[i]=Tx[i]+spread
    prestacao_anual[i]=divida[i]*((1-(1/(1+juro_total[i])))/((1/(1+juro_total[i]))-(1/(1+juro_total[i]))**(anos_em_falta[i]+1)))
    juro_capital_em_divida[i]=juro_total[i]*divida[i]
    amortizacao[i]=prestacao_anual[i]-juro_capital_em_divida[i]
    coltab.append([divida[i], juro_total[i],prestacao_anual[i],juro_capital_em_divida[i],amortizacao[i]])
    
# Criação do DataFrame - tabela
colunas = ['Dívida', 'Juro Total', 'Prestação Anual', 'Juro Capital em Divida','Amortização']
tabela = pd.DataFrame(coltab, columns=colunas)

print(tabela)

#######FIM#######

