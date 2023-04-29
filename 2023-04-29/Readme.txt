Um campo de Markov é um conjunto de variáveis aleatórias em que a distribuição de probabilidade de cada variável é condicional às variáveis vizinhas. O Método de Monte Carlo baseado em Cadeias de Markov (MCMC) é uma técnica estatística usada para aproximar a distribuição de probabilidade de um campo de Markov. Neste exemplo, vou te mostrar como criar um campo de Markov de 2D, ou seja, uma grade, usando MCMC com o algoritmo Metropolis-Hastings em Python.

```python
import numpy as np
import matplotlib.pyplot as plt

def energy(grid):
    return -np.sum(grid * np.roll(grid, 1, axis=0) + grid * np.roll(grid, 1, axis=1))

def metropolis_hastings(grid, beta):
    x, y = np.random.randint(0, grid.shape[0]), np.random.randint(0, grid.shape[1])
    new_grid = np.copy(grid)
    new_grid[x, y] *= -1

    delta_energy = energy(new_grid) - energy(grid)

    if delta_energy <= 0 or np.random.random() < np.exp(-beta * delta_energy):
        return new_grid
    else:
        return grid

def run_simulation(grid_size, n_steps, beta):
    grid = np.random.choice([-1, 1], size=(grid_size, grid_size))
    for _ in range(n_steps):
        grid = metropolis_hastings(grid, beta)
    return grid

grid_size = 10
n_steps = 10000
beta = 0.4

grid = run_simulation(grid_size, n_steps, beta)
plt.imshow(grid, cmap="coolwarm")
plt.show()
```

Este exemplo cria um campo de Markov quadrado de tamanho 10x10 usando o algoritmo Metropolis-Hastings. A função `energy` calcula a energia do campo de Markov, e a função `metropolis_hastings` implementa o passo Metropolis-Hastings. A função `run_simulation` executa a simulação MCMC por um determinado número de passos e retorna a grade final. O exemplo usa uma temperatura fictícia (beta) de 0.4, que controla a probabilidade de aceitar mudanças que aumentam a energia.

-------------

O algoritmo Metropolis-Hastings é um método de Monte Carlo baseado em Cadeias de Markov (MCMC) que tem como objetivo gerar amostras de uma distribuição de probabilidade alvo, especialmente quando é difícil ou impossível obtê-las diretamente. O algoritmo é particularmente útil para lidar com distribuições de alta dimensão e/ou distribuições com uma forma complicada.

O algoritmo Metropolis-Hastings funciona construindo uma cadeia de Markov cuja distribuição estacionária converge para a distribuição de probabilidade alvo. Ele faz isso propondo novos pontos no espaço de amostra com base em um valor atual e aceitando ou rejeitando esses pontos com base em uma regra de aceitação.

A regra de aceitação considera a razão entre as probabilidades da proposta e do ponto atual, bem como a razão entre as probabilidades de transição dos dois pontos. Isso garante que a cadeia de Markov siga uma distribuição estacionária que corresponda à distribuição alvo.

Os principais objetivos do algoritmo Metropolis-Hastings são:

1. Gerar amostras de uma distribuição de probabilidade alvo complexa ou de alta dimensão.
2. Aproximar integrais complexas ou multidimensionais que são difíceis de resolver analiticamente, como em problemas de inferência bayesiana.
3. Explorar eficientemente o espaço de amostra, especialmente em casos onde a distribuição alvo tem várias modas ou uma estrutura complicada.

O algoritmo Metropolis-Hastings é amplamente utilizado em diversas áreas, como física estatística, química computacional, processamento de imagens, aprendizado de máquina e estatísticas bayesianas.