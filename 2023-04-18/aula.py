import random

def generateRandom(threshold = 0.5):
    rnd_value = random.random()
    if ( rnd_value > threshold ):
        return 1
    return 0

def calculate_prob(p1=0, p2=0, dist = [[0.6, 0.1], [0.15, 0.15]]):
    m = 0
    for i in range(len(dist)):
        m += dist[i][p2]
    n = dist[p1][p2] / m

    return n

def main():
    dist = [[0.6, 0.1], [0.15, 0.15]]

    x = generateRandom()
    y = generateRandom()

    accept = False

    while(accept == False):
        x1 = generateRandom()
        alpha = calculate_prob(x1, y, dist)
        accepted = dist[x1][y]
        accept = alpha < accepted
        if (accept):
            print(x1)

if __name__ == "__main__":
    main()