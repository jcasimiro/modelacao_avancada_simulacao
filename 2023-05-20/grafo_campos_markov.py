import networkx as nx
import random
import math
import matplotlib.pyplot as plt

def calculate_energy(graph):
    # Função de energia: calcula a energia total do grafo
    energy = 0
    for edge in graph.edges():
        energy += graph[edge[0]][edge[1]]['weight']  # Exemplo: soma dos pesos das arestas
    return energy

def metropolis_hastings(graph, iterations, temperature):
    for _ in range(iterations):
        # Escolha uma aresta aleatória
        edges = list(graph.edges())
        
        if (len(edges)==0):
            continue

        edge = random.choice(edges)

        # Faça uma alteração na aresta selecionada (por exemplo, adicione ou remova)
        if graph.has_edge(edge[0], edge[1]):
            graph.remove_edge(edge[0], edge[1])
        else:
            graph.add_edge(edge[0], edge[1], weight=random.random())

        # Calcule a variação de energia
        current_energy = calculate_energy(graph)
        graph_copy = graph.copy()
        proposed_energy = calculate_energy(graph_copy)

        energy_diff = proposed_energy - current_energy

        # Aceite ou rejeite a alteração com base na variação de energia e temperatura
        if energy_diff < 0 or random.random() < math.exp(-energy_diff / temperature):
            graph = graph_copy

    return graph

# Exemplo de uso:
# Cria um grafo inicial com 4 vértices formando um quadrado
initial_graph = nx.Graph()
initial_graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)], weight=1.0)

#nx.draw(initial_graph, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
#plt.show()

# Simula o grafo usando o algoritmo Metrópolis-Hastings
simulated_graph = metropolis_hastings(initial_graph, iterations=1000, temperature=1.0)

# Imprime o grafo simulado
pos = nx.spring_layout(simulated_graph)  # Define o layout do gráfico
weights = [simulated_graph[u][v]['weight'] for u, v in simulated_graph.edges()]  # Obtém os pesos das arestas

nx.draw(simulated_graph, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', width=weights)
plt.show()