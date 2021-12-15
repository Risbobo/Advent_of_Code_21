import numpy as np


def process(my_input):
    my_file = open(my_input, 'r')
    lines = my_file.readlines()
    return np.array([[int(x) for x in line.strip()] for line in lines])


def init_phero(mat):
    n, m = np.shape(mat)
    mean = np.mean(mat)
    return np.full((n, m), mean/(n*m))


def ant(start, end, mat, phero, rho=0.9):
    n, m = np.shape(mat)
    path = []
    risk = 0
    current_pos = start
    while current_pos != end:
        possible_next_pos = []
        i, j = current_pos
        if i-1 > 0:
            possible_next_pos.append([i - 1, j])
        if j-1 > 0:
            possible_next_pos.append([i, j - 1])
        if i+1 < n:
            possible_next_pos.append([i + 1, j])
        if j+1 < m:
            possible_next_pos.append([i, j + 1])
        next_pos = decide_next(possible_next_pos, mat, phero)
        path.append(next_pos)
        risk += mat[next_pos[0], next_pos[1]]
        # Update pheromons ?
        phero[next_pos[0], next_pos[1]] *= rho
        current_pos = next_pos
    return path, risk


def explore(mat, phero):
    count = 0
    best_risk = np.inf


def decide_next(poss_next, mat, phero):
    weights = []
    norm = 0
    for poss in poss_next:
        i, j = poss
        weight = 1 / mat[i, j] * phero[i, j]
        weights.append(weight)
        norm += weight
    weights /= norm
    index = np.random.choice(range(len(poss_next)), 1, p=weights)[0]
    return poss_next[index]


def end_pos(mat):
    return [np.shape(mat)[0] - 1, np.shape(mat)[1] - 1]


maze = process('ex_15.txt')
pheromones = init_phero(maze)
print(maze)
print(pheromones)
path, risk = ant([0, 0], end_pos(maze), maze, pheromones)
print(path)
print(risk)
print(pheromones)
