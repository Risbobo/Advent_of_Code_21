from utils import input_reader


def navigate(input):
    instructions = input_reader(input, [str, int])

    coord = [0, 0]
    for instr, dist in instructions:
        if instr == 'forward':
            coord[0] += dist
        elif instr == 'down':
            coord[1] += dist
        elif instr == 'up':
            coord[1] -= dist
        else:
            print("Error : {} is not an instruction".format(instr))
    return coord


# res = navigate('ex_02.txt')
res = navigate('input_02.txt')
print(res)
print(res[0] * res[1])
