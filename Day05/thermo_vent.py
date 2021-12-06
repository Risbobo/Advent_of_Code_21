import numpy as np
import math


def process_input(inpout):
    myFile = open(inpout, 'r')
    lines = myFile.readlines()
    outpout = []
    for line in lines:
        line = line.strip().split(' -> ')
        coords = []
        for coord in line:
            coords.append([int(x) for x in coord.split(',')])
        outpout.append(coords)
    return np.array(outpout)


# Not necessary after all
# Keeping only vertical and horizontal lines
# def simons_mistake(list_of_vents):
#     lines_of_vents = []
#     for line in list_of_vents:
#         if (line[0,0] == line[1,0]) or (line[0,1] == line[1,1]):
#             lines_of_vents.append(line)
#     return np.array(lines_of_vents)


def generate_grid(list_of_vents, part1=True):
    xs, ys = partition_xy(list_of_vents)
    grid_shape = (np.max(xs) + 1, np.max(ys) + 1)
    grid = np.zeros(grid_shape)
    lines = line_generator(list_of_vents, part1)
    for line in lines:
        for i in line[2]:
            # Part 1
            # Horizontal lines
            if line[0] == 0:
                grid[i, line[1]] += 1
            # Vertical lines
            if line[0] == 1:
                grid[line[1], i] += 1
            # Part 2
            # Positive slope diagonals
            if line[0] == 2:
                grid[line[1][1] + i, line[1][0] + i] += 1
            # Negative slope diagonals
            if line[0] == 3:
                grid[line[1][1] - i, line[1][0] + i] += 1
    return grid


def line_generator(list_of_vents, part1=True):
    lines = []
    for line in list_of_vents:
        # horizontal lines
        if line[0, 0] == line[1, 0]:
            low, high = min(line[0, 1], line[1, 1]), max(line[0, 1], line[1, 1])
            lines.append([0, line[0, 0], range(low, high + 1)])
        # vertical lines
        if line[0, 1] == line[1, 1]:
            low, high = min(line[0, 0], line[1, 0]), max(line[0, 0], line[1, 0])
            lines.append([1, line[0, 1], range(low, high + 1)])
        if not part1:
            if abs(line[0, 0] - line[1, 0]) == abs(line[0, 1] - line[1, 1]):
                start = line[0] if line[0, 0] < line[1, 0] else line[1]
                # Positive slope diagonals
                if math.copysign(1, line[0, 0] - line[1, 0]) == math.copysign(1, line[0, 1] - line[1, 1]):
                    lines.append([2, start, range(abs(line[0, 0] - line[1, 0]) + 1)])
                # Negative slope diagonals
                else:
                    lines.append([3, start, range(abs(line[0, 0] - line[1, 0]) + 1)])
    return lines


def partition_xy(list_of_vents):
    xs = []
    ys = []
    for line in list_of_vents:
        xs.append([line[0, 0], line[1, 0]])
        ys.append([line[0, 1], line[1, 1]])
    xs = np.array(xs)
    ys = np.array(ys)
    return xs, ys


def count_grid(grid):
    count = 0
    for line in grid:
        for case in line:
            if case > 1:
                count += 1
    return count


# vents = process_input('ex_05.txt')
vents = process_input('input_05.txt')
line_of_vents = vents
grid = generate_grid(vents, part1=False)
print(grid)
print(count_grid(grid))

