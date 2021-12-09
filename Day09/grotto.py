import numpy as np


def process(my_input):
    my_file = open(my_input, 'r')
    lines = my_file.readlines()
    return np.pad(np.array([[int(x) for x in line.strip()] for line in lines]), ((1, 1), (1, 1)), mode='constant',
                  constant_values=9)


def low_points_index(mat):
    index = []
    # padded = np.pad(mat, ((1, 1), (1, 1)), mode='constant', constant_values=9)
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[0]) - 1):
            if mat[i + 1, j] > mat[i, j] and mat[i - 1, j] > mat[i, j] and mat[i, j + 1] > mat[i, j] \
                    and mat[i, j - 1] > mat[i, j]:
                index.append([i, j])
    return index


def bassin_rec(point, mat, bassin=[]):
    bassin.append(point)
    # print(bassin)
    # print(point)

    i = point[0]
    j = point[1]
    up = mat[i+1, j]
    left = mat[i, j-1]
    right = mat[i, j+1]
    down = mat[i-1, j]
    center = mat[i, j]

    if center < up < 9 and [i+1, j] not in bassin:
        bassin = bassin_rec([i+1, j], mat, bassin)
    if center < left < 9 and [i, j-1] not in bassin:
        bassin = bassin_rec([i, j-1], mat, bassin)
    if center < right < 9 and [i, j+1] not in bassin:
        bassin = bassin_rec([i, j+1], mat, bassin)
    if center < down < 9 and [i-1, j] not in bassin:
        bassin = bassin_rec([i-1, j], mat, bassin)
    return bassin


# matrice = process('ex_09.txt')
matrice = process('input_09.txt')
# print(matrice)
low_point = low_points_index(matrice)
somme = 0
bassins = []
bassin_sizes = []
for point in low_point:
    somme += 1 + matrice[point[0], point[1]]
    b = bassin_rec(point, matrice, [])
    bassin_sizes.append(len(b))
    bassins.append(b)
print(somme)
three_largest = sorted(bassin_sizes)[-3:]
print(np.prod(np.array(three_largest)))
