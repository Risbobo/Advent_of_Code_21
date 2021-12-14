import numpy as np


def process(my_input):
    my_file = open(my_input, 'r')
    line = my_file.readline()
    dots = []
    while line != '\n':
        dots.append([int(x) for x in line.strip().split(',')])
        line = my_file.readline()
    folds = []
    line = my_file.readline()
    while line:
        instr, coord = line.strip().split('=')
        folds.append([0 if instr == 'fold along x' else 1, int(coord)])
        line = my_file.readline()
    return np.array(dots), np.array(folds)


def folding(fold, dots):
    i = fold[0]
    for dot in dots:
        if dot[i] > fold[1]:
            dot[i] = dot[i] - 2 * (dot[i] - fold[1])
    return np.unique(dots, axis=0)


def representation(dots):
    n = max(dots[:, 0]) + 1
    m = max(dots[:, 1]) + 1
    mat = np.full((n, m), ' ')
    for dot in dots:
        mat[dot[0], dot[1]] = '#'
    for line in mat.T:
        print(''.join(line))


# points, pliages = process('ex_13.txt')
points, pliages = process('input_13.txt')
points = folding(pliages[0], points)
print('Answer to part 1 : ', len(points))
print('Answer to part 2 : ')
for pliage in pliages[1:]:
    points = folding(pliage, points)
representation(points)

