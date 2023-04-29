import numpy as np
import matplotlib.pyplot as plt

#calculo da energia
def energy(grid):
    return -np.sum(grid * np.roll(grid, 1, axis=0) + grid * np.roll(grid, 1, axis=1))

#algoritmo metropolis hastings
def metropolis_hastings(grid, beta):
    x, y = np.random.randint(0, grid.shape[0]), np.random.randint(0, grid.shape[1])
    new_grid = np.copy(grid)
    new_grid[x, y] *= -1

    delta_energy = energy(new_grid) - energy(grid)

    #método de aceitação/rejeição
    if delta_energy <= 0 or np.random.random() < np.exp(-beta * delta_energy):
        return new_grid
    else:
        return grid
    
#executar a simulação
def run_simulation(grid_size, n_steps, beta):
    grid = np.random.choice([-1, 1], size=(grid_size, grid_size))
    for _ in range(n_steps):
        grid = metropolis_hastings(grid, beta)
    return grid

grid_size = 3
n_steps = 300
# O racional por trás da escolha do valor de beta está relacionado ao controle da 
# probabilidade de aceitação de novas amostras propostas que resultam em um aumento 
# na energia (ou outra quantidade de interesse). Valores diferentes de beta afetam a 
# dinâmica da cadeia de Markov e, consequentemente, a convergência e a eficiência do algoritmo.

# Beta alto (temperatura baixa): A cadeia é menos propensa a aceitar amostras que aumentam a energia, 
# resultando em um comportamento mais conservador e exploratório, mas também em uma convergência mais 
# lenta e maior autocorrelação entre as amostras.

# Beta baixo (temperatura alta): A cadeia é mais propensa a aceitar amostras que aumentam a energia, 
# o que permite uma maior exploração do espaço de amostra e uma convergência mais rápida. 
# No entanto, um valor de beta muito baixo pode resultar em uma exploração excessiva, dificultando a 
# estabilização da cadeia em torno da distribuição alvo.

# A escolha do valor de beta é geralmente feita por tentativa e erro, com base no conhecimento do 
# problema e nos resultados da simulação. Em alguns casos, pode-se usar técnicas como o "simulated annealing" 
# (arrefecimento simulado), onde o valor de beta é ajustado dinamicamente durante a simulação, começando com 
# valores baixos para explorar o espaço de amostra e gradualmente aumentando para convergir para a 
# distribuição alvo.
beta = 0.7

grid = run_simulation(grid_size, n_steps, beta)
plt.imshow(grid, cmap="coolwarm")
plt.show()