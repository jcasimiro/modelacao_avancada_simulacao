#metropolis
import random

def random_between_zero_and_one():
    return random.random()

def random_between_range(i, j):
    return random.randint(i, j)

def Q_matrix():
    Q = []

    for n in range(0, 3):
        rnd1 = random_between_range(1, 100)
        rnd2 = random_between_range(1, 100)
        rnd3 = random_between_range(1, 100)
        sum = rnd1 + rnd2 + rnd3
        Q.append([rnd1/sum, rnd2/sum, rnd3/sum])

    return Q

def calcular_alpha(q, pi):
    alpha = []
    alpha_line = [-1, -1, -1]
    for i in range(0,3):
        for j in range(0,3):
            tmp = pi[j] * q[j][i] / pi[i] * q[i][j]
            if ( tmp < 1 ):
                alpha_line[j] = tmp
            else:
                alpha_line[j] = 1
        alpha.append(alpha_line)
    return alpha

def calcular_matriz_p(Q, alpha):
    alpha = []
    alpha_line = [-1, -1, -1]
    for i in range(0,3):
        for j in range(0,3):
            tmp = pi[j] * q[j][i] / pi[i] * q[i][j]
            if ( tmp < 1 ):
                alpha_line[j] = tmp
            else:
                alpha_line[j] = 1
        alpha.append(alpha_line)
    return alpha    

def main():
    Q = Q_matrix()
    Pi = [0.3, 0.5, 0.2]
    print(calcular_alpha(Q, Pi))

if __name__ == "__main__":
    main()