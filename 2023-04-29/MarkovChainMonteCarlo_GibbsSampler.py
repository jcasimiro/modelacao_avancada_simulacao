import numpy as np

# Definir a grade
grid_size = 10
grid = np.random.randint(2, size=(grid_size, grid_size))

# Definir a energia do sistema
def calculate_energy(grid):
    energy = 0
    for i in range(grid_size):
        for j in range(grid_size):
            neighbor_sum = grid[(i+1)%grid_size,j] + grid[(i-1)%grid_size,j] + grid[i,(j+1)%grid_size] + grid[i,(j-1)%grid_size]
            energy += (2*grid[i,j] - 1) * neighbor_sum
    return energy

# Implementar o método Gibbs sampler
def gibbs_sampler(grid, beta):
    for i in range(grid_size):
        for j in range(grid_size):
            neighbor_sum = grid[(i+1)%grid_size,j] + grid[(i-1)%grid_size,j] + grid[i,(j+1)%grid_size] + grid[i,(j-1)%grid_size]
            p = 1.0 / (1.0 + np.exp(-2.0*beta*(2*grid[i,j] - 1)*neighbor_sum))
            if np.random.uniform() < p:
                grid[i,j] = 1
            else:
                grid[i,j] = 0
    return grid

# Iterar o Gibbs sampler até que o sistema atinja o equilíbrio
beta = 0.4
for i in range(300):
    grid = gibbs_sampler(grid, beta)

# Retornar a grade com os valores atualizados
print(grid)