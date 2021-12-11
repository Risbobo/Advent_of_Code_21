import numpy as np


def process(my_input):
    my_file = open(my_input, 'r')
    lines = my_file.readlines()
    return np.pad(np.array([[int(x) for x in line.strip()] for line in lines]), ((1, 1), (1, 1)), mode='constant',
                  constant_values=0)


def step(mat):
    synchro = True
    number_of_flash = 0
    explode = []
    # Energy raises
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[0]) - 1):
            mat[i, j] += 1
            if mat[i, j] == 10:
                explode.append([i, j])
                number_of_flash += 1
    # Chain reaction
    while explode:
        point = explode.pop()
        x = point[0]
        y = point[1]
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 < i < len(mat) - 1 and 0 < j < len(mat) - 1 and not (i == x and j == y):
                    mat[i, j] += 1
                    if mat[i, j] == 10:
                        explode.append([i, j])
                        number_of_flash += 1
    # Cleaning
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[0]) - 1):
            if mat[i, j] >= 10:
                mat[i, j] = 0
            if mat[i, j] != 0:
                synchro = False
    return number_of_flash, synchro


matrice = process('input_11.txt')
flashes = 0
steps = 0
synchro = False
while not synchro:
    flash, synchro = step(matrice)
    flashes += flash
    steps += 1
    if steps == 100:
        print(flashes)
print(steps)
