# type_casts must be a list of function (usually type_cast)
# for example with Day 2, it would be [str, int]
def input_reader(input, type_casts=None, line_func=str.split):
    my_file = open(input, 'r')
    lines = my_file.readlines()
    # print(line_func(lines[0]))
    assert len(type_casts) == len(
        line_func(lines[0])), 'Number of type_cast = {} not equal to the number of input per line = {}'.format(
        len(type_casts), len(line_func(lines[0])))
    if type_casts is None:
        type_casts = [lambda x: x] * len(line_func(lines[0]))
    mat_res = [[0 for _ in range(len(type_casts))] for _ in range(len(lines))]
    for i, l in enumerate(lines):
        for j, elem in enumerate(line_func(l)):
            mat_res[i][j] = type_casts[j](elem)
    return mat_res


# Bien sûr que ça existe, mais où est le fun ?
def bin_to_int(b):
    n = 0
    for e, f in enumerate(b) :
        n += int(f)*2**(len(b)-e-1)
    return n


def int_to_bin(i):
    if i == 0:
        return '0'
    bin_val = ""
    m = i
    while m > 0:
        m, r = divmod(m, 2)
        bin_val = str(r) + bin_val
    return bin_val
