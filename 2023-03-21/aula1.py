import random

contar_jogadas = 0
nr_simulacoes = 10**6
contar_ruina = 0
probabilidade = 0.0

for i in range(nr_simulacoes):
    caixa = 5
    while caixa > 0 and caixa < 10:
        n = random.random()
        if ( n > 1/2):
            caixa += 1
        else:
            caixa -= 1
        contar_jogadas += 1
    if caixa == 0:
        contar_ruina += 1

print("caixa: %f" %caixa)
print("jogadas: %i" %contar_jogadas)
print("probabilidade: %f" %(contar_ruina/nr_simulacoes))
